/**
 * schedule.js: Fetch your UoG schedule from WebAdvisor.
 *
 * Author: Nick Presta
 * Copyright: Copyright 2012
 * License: MIT
 * Version: 0.0.1
 * Maintainer: Nick Presta
 * Email: nick@nickpresta.ca
 */

var casper = require('casper').create();
var fs = require('fs'),
    input = fs.open('/dev/stdin', 'r');

if (!casper.cli.options.hasOwnProperty('semester')) {
  var date = new Date();
  var month = date.getMonth();
  var year = date.getYear().toString().substr(1);

  if (month <= 3) {
    // Winter semester - January to April
    casper.cli.options.semester = 'W' + year;
  } else if (month <= 7) {
    // Summer semseter - May to August
    casper.cli.options.semseter = 'S' + year;
  } else {
    // Fall semester - September to December
    casper.cli.options.semseter = 'F' + year;
  }
}

if (!casper.cli.options.hasOwnProperty('username') ||
    !casper.cli.options.hasOwnProperty('password')) {
  casper.cli.options.username = input.readLine();
  casper.cli.options.password = input.readLine();
  if (!casper.cli.options.username || !casper.cli.options.password) {
    casper.echo("You must provide a username and password argument (--username, --password).");
    casper.echo("You may also input the arguments on command line (username first line, password next.");
    casper.exit();
  }
}

// Login
casper.start('https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?TOKENIDX=1631421451&SS=LGRQ', function() {
  this.evaluate(function(username, password) {
    document.querySelector('input#USER_NAME').value = username;
    document.querySelector('input#CURR_PWD').value = password;
    document.querySelector('input[name="SUBMIT2"]').click();
  }, {
    username: casper.cli.options.username,
    password: casper.cli.options.password
  });
});

// Click on "Students"
casper.then(function() {
  this.click('h3 + ul li a.WBST_Bars');
});

// Click on "Class Schedule"
casper.then(function() {
  this.click('a[href$="ST-WESTS13A"]');
});

// Set dropdown to "W12" and submit form
casper.then(function() {
  this.fill('form[name="datatelform"]', {
    'VAR4': casper.cli.options.semester
  }, true);
});

// Grab schedule data
casper.then(function() {
  var data = this.evaluate(function() {
    return window.delimitedMeetingInfo;
  });
  this.echo(data);
});

casper.run(function() {
  casper.exit();
});

