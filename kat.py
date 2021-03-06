#!/usr/bin/python3

print ('Content-type: text/html\n')

Template = '''
<!DOCTYPE html>
<html>
<title>Kat</title>
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
        background-image: url("https://cdnb.artstation.com/p/assets/images/images/003/935/277/large/aiko-san-650bc8226cdfee82e243ef017bbe643e.jpg?1478688456");
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
  "&nbsp; Today's an ordinary day, like any other.<br>&nbsp; I was just about to get out of my bed, when...<button onclick='myFunction0()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV3").innerHTML = " ";
}
function myFunction0() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; *BOOM*<br>&nbsp; *CRASH*<br>&nbsp; Oops!!!";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunctiona()'><input type='submit' value='Get up'></p>"
  document.getElementById("name").innerHTML = " "
}
function myFunctiona() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; <i>*Sigh*<br>&nbsp; I sit there, counting the seconds until she arrives.<br>&nbsp; 1, 2, 3....</i><br><button onclick='myFunction0()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunctionb()' class='button'><span>Next&nbsp;</span></button>";
document.getElementById("myDIV2").innerHTML = ""
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunctionb() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; ONII-CHAN! GET U-<br>&nbsp; ...<br>&nbsp; Oh, you're awake.<br><button onclick='myFunctiona()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction1()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???";
  document.getElementById("myDIV3").innerHTML = "<img src='kat.png' width='500' height='550'>";
}
function myFunction1() {
  document.getElementById("myDIV1").innerHTML = 
  "&nbsp; Yeah, g'mornin, Kat. <br>&nbsp; You took the time to come wake me up? Thanks.<br><button onclick='myFunctionb()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction2()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunction2() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; B-baka! It's not like I came to wake you up or anything...<br>&nbsp; I'm just here to make sure you didn't die in your sleep. <br>&nbsp; Also, come down if you're awake, breakfast is ready! Why do I have to go to your room just to wake <br>&nbsp; you up if you're already awake? <br><button onclick='myFunction1()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction3()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat"
}
function myFunction3() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Sorry Kat, but thanks for making me breakfast.<br><br>&nbsp; <i>I walk up to her, and pat her head.</i><br><br>&nbsp; Shall we go downstairs, then?<br><button onclick='myFunction2()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction4()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction4() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; //// Don't pat me, idiot onii-chan! Hmph! <br><button onclick='myFunction3()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction5()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat"
}
function myFunction5() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Kat ran downstairs and away from me.<br>&nbsp; I slowly follow her down the stairs and into the living room, where Kat's already waiting, preparing <br>&nbsp; breakfast.</i> <br><button onclick='myFunction4()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction6()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://studiomugenjohncel.files.wordpress.com/2010/10/kitchen-table.png' width='1300' height='auto'></p>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction6() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ~~~~??? ???  <br><button onclick='myFunction5()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction7()' class='button'><span>Next&nbsp;</span></button>";
???document.getElementById("name").innerHTML = "&nbsp; Kat"
}
function myFunction7() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>While listening to Kat hum a familiar tune, I reach out for my morning coffee.<br>&nbsp; Kat's my younger sister.</i><br><button onclick='myFunction6()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction8()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction8() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Katherine Aizawa is 4 years younger than I am, but she's a lot more responsible and reliable than me.<br>&nbsp; While I go to college, she goes to high school.<br>&nbsp; Our parents are frequently abroad for work, so ever since we were young, we've stuck together, <br>&nbsp; with just the two of us. </i><br><button onclick='myFunction7()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction9()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction9() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Perhaps it's because Kat's never really had another male approach her, but -<br>&nbsp; I know that she has an affection for me that isn't normal for siblings.<br>&nbsp; She loves me not as just a brother, but in 'that' way.<br>&nbsp; I know that I have to take responsibility, but I'm always running away from my problems.</i><br><button onclick='myFunction8()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction10()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction10() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Whenever Kat gets, well, too close, I tell her that we can't, because we're siblings...<br>&nbsp; But to say the truth, we aren't blood related.<br>&nbsp; Both Kat and I are adopted. My parents were both too busy to make a child of their own, so they <br>&nbsp; adopted us instead of making their own kid.<br>&nbsp; Of course, I'm the only one who knows about this. Kat doesn't, and I've never told her.</i> <br><button onclick='myFunction9()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction11()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction11() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Hey, onii-chan. Let's go on a date today.";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunction12a()'><input type='submit' value='Umm... sure, why not?'></p><br><br><p onclick='myFunction12b()'><input type='submit' value='Wha-what? Umm, sorry Kat, not today.'></p>"
  document.getElementById("name").innerHTML = "&nbsp; Kat"
}
function myFunction12a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>A date? What's she thinking?<br>&nbsp; Kat has her back turned, but it's clear that she's blushing, since the tip of her ears are bright red.<br>&nbsp; That surprised me, though, enough for me to nearly spit out my coffee...<br>&nbsp; But there's really no reason for me to say no, so why not just stick with Kat for a day, right?</i><button onclick='myFunction13a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " "
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction13a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Hey Kat? Where you wanna go?<br><br>&nbsp; <i>Kat jumps up a bit, like she wasn't expecting to hear an answer of approval.</i><br><button onclick='myFunction12a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction14a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction14a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; U-Umm... how about the amusement park?...<br><br>&nbsp; But, don't get me wrong! It's not like I want to have fun in the amusement park with you, onii-chan!<br>&nbsp; It's just that I haven't seen you have fun outside for a while, so I have no choice but to give you a <br>&nbsp; chance to enjoy yourself.../// <br><button onclick='myFunction13a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction15a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat"  
}
function myFunction15a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>She hasn't gotten rid of her habit of being a tsundere.<br>&nbsp; Honestly, I know that her tsundere is a way for her to hide her honesty.<br>&nbsp; Grinning, I say:</i><br><br>&nbsp; Yeah, I know. Thanks.<br><br>&nbsp; <i>I give her another pat on the head.<br>&nbsp; Kat loves it when I do this - she squints her eyes pleasurably, like an actual cat.</i><br><button onclick='myFunction14a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction16a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction16a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, how 'bout we pack ourselves to go?<br><button onclick='myFunction15a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction17a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction17a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; A-already? It's still pretty early, you know.<br><button onclick='myFunction16a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction18a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat"  
}
function myFunction18a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, the earlier, the better! We'd be able to have the rides all to ourselves.<br>&nbsp; C'mon Kat, let's go!<br><button onclick='myFunction17a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction19a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction19a() {
  document.getElementById("myDIV1").innerHTML =  "";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunction20a()'><input type='submit' value='To the amusement park!'></p>"
}
function myFunction20a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Here we are!<br><br>&nbsp; <i>After around thirty minutes of me driving, we arrive at the park. </i><br><button onclick='myFunction19a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction21a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " ";  
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://i.pinimg.com/474x/37/f1/bf/37f1bfd3859d57c7a6230a32446d0fbb.jpg' width='1300' height='1000'></p>";
}
function myFunction21a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Onii-chan, look! There's cotton candy, ice cream, roller coasters, teacups, bunny mascots...<br><button onclick='myFunction20a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction22a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat"  
}
function myFunction22a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Kat suddenly stops speaking.</i><br><br>&nbsp; Kat? What's wrong?<br><button onclick='myFunction21a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction23a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction23a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; //////B-baka!///////<br>&nbsp; It's not like I'm excited because I'm at the amusement park with you, okay?!<br><button onclick='myFunction22a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction24a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction24a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; All right, all right.<br><br>&nbsp; <i>Another one of Kat's tsunderes.</i><br><br>&nbsp; Well, what should we ride first, princess? <br><button onclick='myFunction23a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction25a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction25a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; The roller coaster!<br><button onclick='myFunction24a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction26a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction26a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Kat grabs my arm and pulls me towards the roller coasters.<br>&nbsp; Usually, she's more the adult than I am; but in times like this, she seems like any other child.</i><br><button onclick='myFunction25a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction27a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction27a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Hours later...<br><button onclick='myFunction26a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction28a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "" 
}
function myFunction28a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, that was fun, wasn't it, onii-chan!<br><button onclick='myFunction27a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction29a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://66.media.tumblr.com/5928b57817284dc27240f027a5abb50c/tumblr_onxpypU3gM1uc9x1zo1_1280.jpg' width='1300' height='1000'></p>";
}
function myFunction29a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Kat and I practically rode all the rides in the park - at least twice.<br>&nbsp; At my age, that's pretty harsh. I'm exhausted, but at least Kat looks like she enjoyed her time here.</i><br><br>&nbsp; Yeah, it was great. I'm glad to see that you had fun too, Kat.<br><button onclick='myFunction28a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction30a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction30a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; /////Yeah, well... thanks, onii-chan.////<br><button onclick='myFunction29a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction31a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction31a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; No problem, love.<br><button onclick='myFunction30a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction32a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction32a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Uhh... onii-chan?<br><button onclick='myFunction31a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction33a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction33a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Yes, dear?<br><br>&nbsp; <i>Kat's a bit restless... is she hesitating from saying something?</i><br><br>&nbsp; Kat? You alright? Need to go pee? *chuckle*<br><button onclick='myFunction32a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction34a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction34a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ?!?!?!?! Oh my GOD, onii-chan! How can you say that to a girl!<br>&nbsp; No, I don't need to go to the bathroom, baka.<br>&nbsp; It's just... just -<br><button onclick='myFunction33a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction35a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction35a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Just what?<br><button onclick='myFunction34a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction36a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction36a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Can we go to one more place? Please? <br><button onclick='myFunction35a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction37a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction37a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I'm kinda surprised. Kat usually doesn't plead for anything.<br>&nbsp; I guess the other place is pretty important to her.</i><br><br>&nbsp; Sure, let's go.<br><button onclick='myFunction36a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction38a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction38a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Riding the car for another 15 minutes, we arrive at the place Kat was referring to.</i><br><button onclick='myFunction37a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction39a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://i.pinimg.com/originals/26/4e/b3/264eb301f8dccc71c588604be6f2a8f9.png' width='1300' height='1000'></p>";
}
function myFunction39a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Wow, it's great view here, Kat. How'd you find this place?<br><button onclick='myFunction38a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction40a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction40a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>No response.</i><br><br>&nbsp; ...Kat?<br><button onclick='myFunction39a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction41a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction41a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Kat's looking down at her fingers, fidgeting. She looks uncomfortable.</i><br><br>&nbsp; Katherine, tell me what's on your mind.<br><button onclick='myFunction40a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction42a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction42a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Wh-what?!....<br>&nbsp; Oh, sorry onii-chan.<br>&nbsp; Umm... onii-chan, will you listen carefully to what I'm about to say?<br><button onclick='myFunction41a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction43a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction43a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>*Badump, badump.*<br>&nbsp; I hear my heartbeat getting faster.<br>&nbsp; Crap, I know this situation. Kat's planning to confess to me again.<br>&nbsp; I should stop her, but... she just looks so hurt.</i><br><button onclick='myFunction42a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction44a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction44a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Onii-chan, I --- <br><button onclick='myFunction43a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction45a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction45a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Kat, wai-<br><button onclick='myFunction44a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction46a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction46a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; I love you.<br>&nbsp; I know it isn't normal for a little sister to like her older brother like this, but... But - I just can't stop <br>&nbsp; it. I'm sorry.<br><button onclick='myFunction45a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction47a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat" 
}
function myFunction47a() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; Kat, I- ";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunction48a()'><input type='submit' value='We...are siblings.'></p>"
}
function myFunction48a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Onii-chan, I know...<br><button onclick='myFunction47a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction49a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat";
  document.getElementById("myDIV2").innerHTML = " "
}
function myFunction49a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Know?</i><br><br>&nbsp; Know what? <br><button onclick='myFunction48a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction50a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunction50a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; We aren't actual siblings, are we?<br><button onclick='myFunction49a()' class='button2'><span>&nbsp;Previous</span></button><a href='kat-happy.html'><button class='button'><span>Next&nbsp;</span></button></a>";
  document.getElementById("name").innerHTML = "&nbsp; Kat";
}

function myFunction12b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Um... sorry Kat. Not today.<br><button onclick='myFunction11()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction13b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " "
}
function myFunction13b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Why not?! I hate you, onii-chan! BAKA!<br><button onclick='myFunction12b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction14b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat "
}
function myFunction14b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Kat runs out of the house, crying.</i><br><br>&nbsp; Kat, wait! <br><br>&nbsp; <i>I run right behind her, catching up.</i><br><button onclick='myFunction13b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction15b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Kat "
}
function myFunction15b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>*Screech*</i><br><button onclick='myFunction14b()' class='button2'><span>&nbsp;Previous</span></button><a href='kat-bad.html'><button class='button'><span>Next&nbsp;</span></button></a>";
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
import sys
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
def main():
    form=cgi.FieldStorage()
    HTML = Template
    name=form.getvalue('name','(nothing)')
    HTML=HTML.replace('???name???',name)     
    print(HTML) 
main()
