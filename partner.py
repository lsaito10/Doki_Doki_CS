#!/usr/bin/python3

print ('Content-type: text/html\n')

Template = '''
<!DOCTYPE html>
<html>
<title>Who's Your Waifu?</title>
<link rel="icon" href="dokidoki.png">
<meta charset="UTF-8">
<meta name="author" content="Lynca">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="csproject.css">

<style>
html, body
{
    height: 100%;
    margin:0;
    padding:0;
}
body {overflow-x: hidden;}
body,h1,h2,p {font-family: "Chalkduster", sans-serif}
img:hover{opacity: 0.6; transition: 0.3s; margin-bottom: -7px}
.w3-row-padding img {margin-bottom: 12px}

body{
        background-image: url("http://i.imgur.com/rfREvdt.jpg");
        background-repeat: no-repeat;
        background-size: 100% 100%;
	align-items: center;
	align-content: center;
	align-self: center;
}

nav {background-color:#cccccc
}

.text {		
				margin-top: 25px;
				margin-left: 50px;
				margin-bottom: 50px;
				display: block;
				height: 100px;
				width: 300px;
				background: white;
				color: black;
				text-align: center;
				-webkit-border-radius: 50px;
				border-radius: 50px;
			}
			p {
				text-align: center;
				color: black;
			}
			.questions {
				display: inline-block;
			}
			.all {
				text-align:right;
				vertical-align: middle; 
			}
			#box {
				background-color: #d7dae0;
				width: 600px;
				margin-top: 100px;
				margin-left: auto;
				margin-right: auto;
				border-radius: 25px;
			}
			
input[type=text] {
  width: 80%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

input[type=submit]{
  background-color: #3399ff;
  border: none;
  color: white;
  padding: 16px 32px;
  text-decoration: none;
  margin: 4px 2px;
  cursor: pointer;
}
input[type=submit]:hover{opacity: 0.6; transition: 0.3s}
</style>
<body>

<nav>
<div class="w3-top">
  <div class="w3-bar w3-black w3-card-2">
    <a href="home.html" class="w3-bar-item w3-button w3-padding-large"><i class="fa fa-home w3-margin-right"></i>HOME</a>
    <a href="intro.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">SITE WALKTHROUGH</a>
    <a href="partner.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">STORY QUIZ</a>
    <a href="characters.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">MADLIBS GENRES</a>
    <a href="creds.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">CREDITS</a>
  </div>
</div>
</nav>

	<div id="box">
		<div class="all">
		<center><br>
		<h2>Your Waifu Is...</h2><br>
			<h1>???Waifu???</h1>
		</center>
</div>
</div>
<br><br><br><br><br>
<script>
var trailLength = 8 
var path = "http://www.javascriptkit.com/script/script2/cursor.gif" 

var standardbody=(document.compatMode=="CSS1Compat")? document.documentElement : document.body 
var i,d = 0

function initTrail() { 
	images = new Array() 
	for (i = 0; i < parseInt(trailLength); i++) {
		images[i] = new Image()
		images[i].src = path
	}
	storage = new Array() 
	for (i = 0; i < images.length*3; i++) {
		storage[i] = 0
	}
	for (i = 0; i < images.length; i++) { 
		document.write('<div id="obj' + i + '" style="position: absolute; z-Index: 100; height: 0; width: 0"><img src="' + images[i].src + '"></div>')
	}
	trail()
}
function trail() { 
	for (i = 0; i < images.length; i++) { 
		document.getElementById("obj" + i).style.top = storage[d]+'px' 
		document.getElementById("obj" + i).style.left = + storage[d+1]+'px' 
		d = d+2
	}
	for (i = storage.length; i >= 2; i--) { 
		storage[i] = storage[i-2]
	}
	d = 0 
	var timer = setTimeout("trail()",10) 
}
function processEvent(e) { 
	if (window.event) { 
		storage[0] = window.event.y+standardbody.scrollTop+10
		storage[1] = window.event.x+standardbody.scrollLeft+10
	} else {
		storage[0] = e.pageY+12
		storage[1] = e.pageX+12
	}
}

	initTrail() 
	document.onmousemove = processEvent
</script>	
</body>
</html>
'''
import cgi
import cgitb
cgitb.enable()
def main():
    form=cgi.FieldStorage()
    HTML = Template
    Clare = 0
    Kat = 0
    Jenny = 0
    Laura = 0
    breaks = form.getvalue("break",'')
    react = form.getvalue("react",'')
    personality = form.getvalue("personality",'')
    genie = form.getvalue("genie",'')
    aspect = form.getvalue("aspect",'')
    listo = []
    listo.append(breaks)
    listo.append(react)
    listo.append(personality)
    listo.append(genie)
    listo.append(aspect)
    fins = []
    for x in listo:
        if x == "Clare":
            Clare += 1
        if x == "Kat":
            Kat += 1
        if x == "Jenny":
            Jenny += 1
        if x == "Laura":
            Laura += 1
    fins.append(Clare)
    fins.append(Kat)
    fins.append(Jenny)
    fins.append(Laura)
    fins.sort()
    C = "Clare!<br><h3><a href='clare.html'><img src='https://media.giphy.com/media/YFFG4W2MvihirVoSQU/giphy.gif' alt='HTML tutorial' style='width:150px;height:100px;border:0'></a>and begin your story!</h3>"
    K = "Kat!<br><h3><a href='kat.html'><img src='https://media.giphy.com/media/YFFG4W2MvihirVoSQU/giphy.gif' alt='HTML tutorial' style='width:150px;height:100px;border:0'></a>and begin your story!</h3>"
    J = "Jenny!<br><h3><a href='jenny.html'><img src='https://media.giphy.com/media/YFFG4W2MvihirVoSQU/giphy.gif' alt='HTML tutorial' style='width:150px;height:100px;border:0'></a>and begin your story!</h3>"
    L = "Laura!<br><h3><a href='laura.html'><img src='https://media.giphy.com/media/YFFG4W2MvihirVoSQU/giphy.gif' alt='HTML tutorial' style='width:150px;height:100px;border:0'></a>and begin your story!</h3>"
    
    waifu = {Clare:C,Kat:K,Jenny:J,Laura:L}
    HTML = HTML.replace('???Waifu???',waifu[fins[-1]])
    print(HTML)
    
main()
    
    
        
        

        
        
        
        
    
