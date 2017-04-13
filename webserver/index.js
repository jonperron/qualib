/*
Quali'B Webserver - Mars 2017
*/

// Import part
var react = require('react');
var express = require('express');
var hogan = require('hogan-express');

// Express
const app = express()
app.engine('html', hogan)
app.set('views', __dirname + '/views')
app.use('/', express.static(__dirname + '/public'))
app.set('port', (process.env.PORT || 8100))

app.get('*',(req, res) => {
	res.status(200).render('index.html')
})

app.listen(app.get('port'))