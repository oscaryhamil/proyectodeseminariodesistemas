var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'TriviaOnline.com' });
});
router.get("/Saladechat/",function(req,res){
	res.render('Saladechat',{title:"Crear partida"});
});
module.exports = router;
