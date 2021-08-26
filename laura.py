#!/usr/bin/python3

print ('Content-type: text/html\n')

Template = '''
<!DOCTYPE html>
<html>
<title>Laura</title>
<link rel="icon" href="dokidoki.png">
<meta charset="UTF-8">
<meta name="author" content="Lynca">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
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
div, h1, h2, h3, p {font-family: "Chalkduster", sans-serif}

body{
        background-image: url("https://data.whicdn.com/images/309844927/original.jpg");
        background-repeat: no-repeat;
        background-size: 100% 100%;
	align-items: center;
	align-content: center;
	align-self: center;
}

nav {background-color:#cccccc;
}

.footer {
   position: fixed;
   left: 10%;
   right: 10%;
   bottom: 10%;
   width: 80%;
   background-color: rgba(255, 255, 255, 0.6);   
   border: 2px solid white;
   border-radius: 25px;
   color: black;
   text-align: left;
}
.button {
  float: right;
  border-radius: 2px;
  border: 2px solid white;
  background-color: transparent;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 20px;
  padding: 8px;
  width: 100px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}
.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: '>>';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -8px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 8px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}
.button2 {
  float: left;
  border-radius: 2px;
  border: 2px solid white;
  background-color: transparent;
  border: none;
  color: #FFFFFF;
  text-align: center;
  font-size: 20px;
  padding: 8px;
  width: 100px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}
.button2 span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button2 span:before {
  content: '<<';
  position: absolute;
  opacity: 0;
  top: 0;
  left: -8px;
  transition: 0.5s;
}

.button2:hover span {
  padding-left: 8px;
}

.button2:hover span:before {
  opacity: 1;
  left: 0;
}
input[type=submit]{
  background-color: white;
  border: none;
  border-radius: 25px;
  color: black;
  padding: 16px 32px;
  text-decoration: none;
  margin: 4px 2px;
  cursor: pointer;
}
input[type=submit]:hover{opacity: 0.6; transition: 0.3s}
.centered {
    position: fixed;
    top: 45%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>
<body>

<p class="centered" id="myDIV4"></p>
<p class="centered" id="myDIV3"></p>
<center><p class="centered" id="myDIV2"></p></center>

<nav>
<div class="w3-top">
  <div class="w3-bar w3-black w3-card-2">
    <a href="home.html" class="w3-bar-item w3-button w3-padding-large"><i class="fa fa-home w3-margin-right"></i>HOME</a>
    <a href="intro.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">DOKI DOKI CS CLUB?</a>
    <a href="partner.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">YOUR WAIFU</a>
    <a href="characters.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">THE CHARACTERS</a>
    <a href="creds.html" class="w3-bar-item w3-button w3-padding-large w3-hide-small">CREDITS</a>
  </div>
</div>
</nav>

<div class="footer">
<h3 id="name">&nbsp; ???name???</h3>
<p id="myDIV1">&nbsp; Hey there, I'm ???name???.<br>
    &nbsp; That's right. I'm you, but stuck in this world.<br>
    &nbsp; I'm also part of the CS club in my school.
    <button onclick="myFunction()" class="button"><span>Next&nbsp;</span></button></p>
</div>

<script>
function myFunction() {
  document.getElementById("myDIV1").innerHTML = 
  "&nbsp; Ohhh... it's senpai...<button onclick='myFunction0()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ??? "
}
function myFunction0() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Here we go again.<br>&nbsp; Hiding in the corner is Laura Yoshida.<br>&nbsp; She's my kouhai (underclassmen), and she, well, is very... affectionate towards me.</i><button onclick='myFunctiona()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunctiona() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Laura, how 'bout you just come out and sit next to me?<br><button onclick='myFunction0()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunctionb()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunctionb() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Eh?! Ah - oh - s-s-s-s-s-s-s-senpai!<br>&nbsp; How did you notice I was here...?<br><button onclick='myFunctiona()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction1()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura";
  document.getElementById("myDIV3").innerHTML = "<img src='laura.png' width='500' height='550'>";
}
function myFunction1() {
  document.getElementById("myDIV1").innerHTML = 
  "&nbsp; <i>Laura slowly comes out of the corner, shoulders rounded, seeming afraid.<br>&nbsp; If she had dog ears, they'd probably be drooping down in apology. </i><br><br>&nbsp; I heard you say my name. <br><button onclick='myFunctionb()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction2()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunction2() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Oh...<br>&nbsp; I-I-I-I'm sorry, senpai... I didn't know how I could get closer to you, and -<br><button onclick='myFunction1()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction3()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura"
}
function myFunction3() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; It's fine, Laura. But next time, just come up to me and talk to me, okay?<br><button onclick='myFunction2()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction4()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction4() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; I'll try...<br><button onclick='myFunction3()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction5()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura"
}
function myFunction5() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The bell, signifying the start to the next class, rings.</i> <br><button onclick='myFunction4()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction6()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = ""
}
function myFunction6() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; W-Well, I'll get going, ???name???-senpai.<br>&nbsp; Goodbye! <br><button onclick='myFunction5()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction7()' class='button'><span>Next&nbsp;</span></button>";
　document.getElementById("name").innerHTML = "&nbsp; Laura"
}
function myFunction7() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Bye~~~ <br><br>&nbsp;<i> I flutter my hand as a goodbye towards Laura. <br>&nbsp; She smiles back, and runs off to her own classroom.</i> <br><button onclick='myFunction6()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction8()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction8() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <br><button onclick='myFunction7()' class='button2'><span>&nbsp;Previous</span></button>";
  document.getElementById("myDIV2").innerHTML =  "<p onclick='myFunction9()'><input type='submit' value='After school...'></p>"
}
function myFunction9() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>School's over. Another day of nothingness has ended.<br>&nbsp; Usually, I'd be on my way to CS Club, but we didn't have any club activities today, so I packed my <br>&nbsp; stuff to get on my way home.</i><br><button onclick='myFunction8()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction10()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML =  ""
  document.getElementById("myDIV3").innerHTML =  ""
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://i.vimeocdn.com/video/593899621_1280x720.jpg' width='1300' height='900'></p>"; 
}
function myFunction10() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Maybe I should go to the supermarket for groceries...<br><br>&nbsp; <i>I mumbled, planning for dinner, when I heard a rustle nearby.</i><br><button onclick='myFunction9()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction11()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction11() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>?????<br>&nbsp; My shoulders jump up in surprise, but I let the incident pass by, thinking it isn't too important.<br>&nbsp; I continue on my way home.</i><br><button onclick='myFunction10()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction12a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML =  ""
}
function myFunction12a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Click, clack......</i><br><button onclick='myFunction11()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction13a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction13a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I was continuing to walk on my way home when I began to hear footsteps.<br>&nbsp; Strange; at around this area at this time, I should be the only one walking.<br><br>&nbsp; I gather my courage to say,</i><br><button onclick='myFunction12a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction14a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction14a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Hello?<br><button onclick='myFunction13a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction15a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML =  "&nbsp; ???name???"
}
function myFunction15a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>No response.<br>&nbsp; I walk further on, then stop.<br>&nbsp; When I walk, the other person walks; when I stop, they stop.<br><br>&nbsp; Crap; I'm being followed. A stalker.<br><br>&nbsp; Thinking that I need to do something, I begin running at max speed to home.<br>&nbsp; I'm too afraid to even look back.</i><br><button onclick='myFunction14a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction16a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML =  ""
}
function myFunction16a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The moment I arrive home, I slam the door behind me.</i><br><br>&nbsp I'm just imagining things. Yeah.<br><br>&nbsp; <i>I try to convince myself, but my hands are shaking.</i><br><button onclick='myFunction15a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction17a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML =  "&nbsp; ???name???"
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/bb73bc48-dc10-450a-9236-15285a9883d2/db39nke-45920d3e-1fc1-4047-bdf2-51b32f8bf146.jpg/v1/fill/w_800,h_415,q_75,strp/living_room_dusk___visual_novel_background_by_giaonp_db39nke-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDE1IiwicGF0aCI6IlwvZlwvYmI3M2JjNDgtZGMxMC00NTBhLTkyMzYtMTUyODVhOTg4M2QyXC9kYjM5bmtlLTQ1OTIwZDNlLTFmYzEtNDA0Ny1iZGYyLTUxYjMyZjhiZjE0Ni5qcGciLCJ3aWR0aCI6Ijw9ODAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.iKYAmUhBNbIYc7F-yKzBBXT2vEu-LzbIruSn7VsvWME' width='1300' height='900'></p>"; 
}
function myFunction17a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; I... should sleep. I have school tomorrow, anyway, hehehe...<br><br>&nbsp; <i>Exhausted from running away from the stalker, I go to bed, in hopes that everything is just a bad<br>&nbsp; dream.</i><br><button onclick='myFunction16a()' class='button2'><span>&nbsp;Previous</span></button>";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunction18a()'><input type='submit' value='Go to bed.'></p>"
}
function myFunction18a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The next day, I arrive to school, like always, greeting my friends and slouching into my chair.</i><br><button onclick='myFunction17a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction19a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV4").innerHTML = ""; 
  document.getElementById("myDIV2").innerHTML = " ";  
}
function myFunction19a() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; Senpai... He's so cool, as always...////<br><button onclick='myFunction18a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction20a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???"; 
}
function myFunction20a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Laura. She's watching again, isn't she?</i><br><br>&nbsp; Laura?<br><button onclick='myFunction19a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction21a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV3").innerHTML = "<img src='laura.png' width='500' height='550'>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction21a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Y-yes! Senpai!<br><button onclick='myFunction20a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction22a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura"  
}
function myFunction22a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; C'mon, don't just watch me there. <br>&nbsp; Come sit next to me. <br><br>&nbsp; <i>I tap the seat next to me.</i><br><button onclick='myFunction21a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction23a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction23a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>In slow and careful footsteps, Laura comes next to me and sits down.</i><br><button onclick='myFunction22a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction24a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction24a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Hey, Laura? Am I that unapproachable?<br><button onclick='myFunction23a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction25a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction25a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; What?!<br>&nbsp; Oh, of course not!<br>&nbsp; It's just - just... you're too perfect for someone like me to deserve to be near...<br><button onclick='myFunction24a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction26a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction26a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; That's not true. I enjoy having you as company.<br><button onclick='myFunction25a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction27a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction27a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; R-really? Senpai is so nice...<br><button onclick='myFunction26a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction28a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction28a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>A few minutes pass, and Laura and I enjoy our conversation.<br>&nbsp; At first, Laura seemed nervous speaking to me, but she has opened up to me more.</i><br><button onclick='myFunction27a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction29a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction29a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Oh yeah, Laura.<br><button onclick='myFunction28a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction30a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction30a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Yes, senpai?<br><button onclick='myFunction29a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction31a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction31a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; You should be careful on your way home. There's a stalker walking around in town recently.<br>&nbsp; Just yesterday, I was nearly followed all the way home. <br><button onclick='myFunction30a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction32a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction32a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; R-really? W-wow... you should be careful too, senpai. Ehehe...<br><button onclick='myFunction31a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction33a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction33a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Am I overthinking, or did Laura avert her eyes when I just mentioned that?</i><br><button onclick='myFunction32a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction34a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction34a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; S-senpai?<br><button onclick='myFunction33a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction35a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction35a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Yeah?<br><button onclick='myFunction34a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction36a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction36a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Uh-umm... would you mind walking home with me today?<br>&nbsp; Hearing about that stalker has gotten me afraid of walking alone... <br><button onclick='myFunction35a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction37a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction37a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>No wonder. I'd be afraid, if I were Laura, too.</i><br><br>&nbsp; Yeah, sure.<br>&nbsp; I'll send you home.<br><button onclick='myFunction36a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction38a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction38a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Thank you so much, ???name???-senpai!<br><button onclick='myFunction37a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction39a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction39a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Laura and I walk towards her house.<br>&nbsp; The skies begin getting cloudy.<br><button onclick='myFunction38a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction40a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://studiomugenjohncel.files.wordpress.com/2012/10/urban_day.jpg' width='1300' height='900'></p>"; 
}
function myFunction40a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, at least no one has followed us.<br>&nbsp; Alright, Laura, I'll be on my way back to my house.<br><button onclick='myFunction39a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction41a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction41a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Are you sure you'll be alright, senpai? <br><button onclick='myFunction40a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction42a()' class='button'><span>Next&nbsp;</span></button>"
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction42a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Yeah, just don't worry.<br>&nbsp; See you, Laura!<br><button onclick='myFunction41a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction43a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ??name???"
}
function myFunction43a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Just as I was about to turn my back on Laura and walk home, rain began to pour.</i><br><button onclick='myFunction42a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction44a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction44a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; You've gotta be kidding me...<br><button onclick='myFunction43a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction45a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction45a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; S-senpai...<br>&nbsp; <br><button onclick='myFunction44a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction46a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction46a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, I guess I'll just run home then!<br><button onclick='myFunction45a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction47a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction47a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Wait, senpai!<br><button onclick='myFunction46a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction48a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura" 
}
function myFunction48a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Yeah?....<br><br>&nbsp; Achoo!<br><button onclick='myFunction47a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction49a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunction49a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Please come into my house! <br>&nbsp; You'll catch a cold if you run home like that...<br><button onclick='myFunction48a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction50a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura";
}
function myFunction50a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; You sure?<br><br><br>&nbsp; <i>Laura nods aggressively.</i><br><button onclick='myFunction49a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction51a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunction51a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Should I...?</i><br><button onclick='myFunction50a()' class='button2'><span>&nbsp;Previous</span></button>";
  document.getElementById("myDIV2").innerHTML = 
  "<p onclick='myFunction52a()'><input type='submit' value='I would catch a cold... and if I can get into her house, the better!'></p><br><br><p onclick='myFunction52b()'><input type='submit' value='Naw, Laura seems a bit mysterious... Return home.'></p>";
}
function myFunction52a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Laura pushes me into her house.<br>&nbsp; She's keeping it clean.<br><button onclick='myFunction51a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction53a()' class='button'><span>Next&nbsp;</span></button>"
  document.getElementById("myDIV2").innerHTML = ""
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://cdnb.artstation.com/p/assets/images/images/015/412/203/large/riandita-dwi-rumah-sore.jpg?1548239566' width='1300' height='900'></p>"; 
}
function myFunction53a() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; Laura tells me to go up into her room.<br><button onclick='myFunction52a()' class='button2'><span>&nbsp;Previous</span></button>"
  document.getElementById("myDIV2").innerHTML =
  "<p onclick='myFunction54a()'><input type='submit' value='Go up to her room'></p>";
}
function myFunction54a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Eh---<br><button onclick='myFunction53a()' class='button2'><span>&nbsp;Previous</span></button><a href='laura-happy.html'><button class='button'><span>Next&nbsp;</span></button></a>";
  document.getElementById("myDIV2").innerHTML = ""
}

function myFunction52b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Laura's honestly REALLY creepy, so I decide to just go home.</i><br><button onclick='myFunction51a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction53b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " "
}
function myFunction53b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Sorry Laura, I'll be on my way home<br>&nbsp; I'd feel bad if you would have to take care of me, anyway.<br>&nbsp; Thanks though. Bye!!!<br><button onclick='myFunction52b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction54b()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction54b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Senpai, wait ---<br><button onclick='myFunction53b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction55b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Laura"
}
function myFunction55b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I run away.</i><br><button onclick='myFunction54b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction56b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name??? "
}
function myFunction56b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Senpai...<br>&nbsp; Fufufu... wait for me...<br><button onclick='myFunction55b()' class='button2'><span>&nbsp;Previous</span></button><a href='laura-bad.html'><button class='button'><span>Next&nbsp;</span></button></a>";
  document.getElementById("name").innerHTML = "&nbsp; Laura "
}
///

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
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
def main():
    form=cgi.FieldStorage()
    HTML = Template
    name=form.getvalue('name','(nothing)')
    HTML=HTML.replace('???name???',name)     
    print(HTML) 
main()
