// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2025-02-19
// @description  try to take over the world!
// @author       You
// @match        http://10.6.18.2/*
// @icon         http://10.6.18.2/static/images/logo.png
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    document.getElementById('username').value='';//Your username
    document.getElementById('password').value='275059';//Your password
    var login = document.getElementById('login');
    login.click();
    // Your code here...
})();