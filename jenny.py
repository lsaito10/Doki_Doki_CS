#!/usr/bin/python3

print ('Content-type: text/html\n')

Template = '''
<!DOCTYPE html>
<html>
<title>Jenny</title>
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
  "&nbsp; Today's an ordinary day, like any other.<br>&nbsp; I'm stuck in school, bored as hell, sitting in the corner of the classroom towards the windows.<button onclick='myFunction0()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction0() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; Oh! Sorry! I'm so sorry! Ahhh... why am I so careless?<button onclick='myFunctiona()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ??? "
}
function myFunctiona() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; <i>The door opens quite aggressively.</i><br><button onclick='myFunction0()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunctionb()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "";
}
function myFunctionb() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; Good morning, everyone!<br><button onclick='myFunctiona()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction1()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???";
  document.getElementById("myDIV3").innerHTML = "<img src='jenny.png' width='500' height='550'>";
}
function myFunction1() {
  document.getElementById("myDIV1").innerHTML = 
  "&nbsp; <i>Ugh. Great timing for the annoying one to appear.</i> <br><button onclick='myFunctionb()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction2()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunction2() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Good morning, ???name???-kun! A fine morning, isn't it?<br><button onclick='myFunction1()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction3()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"
}
function myFunction3() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Yeah sure, whatever.<br><br>&nbsp; <i>This is Jenny Sakura. I've known her ever since I was born.<br>&nbsp; When we were younger, she was always hiding behind my back, but now, she acts like the leader.<br>&nbsp; Excellent grades, great at sports, also cute and popular with both girls and guys.</i><br><button onclick='myFunction2()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction4()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction4() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Jenny's the class president right now, and she sits right next to me. <br>&nbsp; The other guys aren't really happy 'bout that, but it ain't my fault.</i><br><button onclick='myFunction3()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction5()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction5() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>What about me???... Well, I'm one of those scums -<br>&nbsp; I cut class everyday, pick fights at others (I don't bully), and have pretty foul language.<br>&nbsp; Don't ask me why; it's a pain to explain.<br><br>&nbsp; Anyway, because I'm like this, I've got no friends, and I don't intend on making any.<br>&nbsp; My classmates are mostly afraid of me.<br>&nbsp; Out of those people though, Jenny's the only one who speaks to me; probably just because she thinks <br>&nbsp; she's obligated to since I'm her childhood friend.<br>&nbsp; How idiotic.</i> <br><button onclick='myFunction4()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction6()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction6() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; !!! ???name???-kun, you picked a fight at someone again, didn't you?  <br><button onclick='myFunction5()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction7()' class='button'><span>Next&nbsp;</span></button>";
???document.getElementById("name").innerHTML = "&nbsp; Jenny"
}
function myFunction7() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Yeah, so? <br><button onclick='myFunction6()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction8()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction8() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; You're hurt, and bruised! You have to go to the nurse's offi-<br><button onclick='myFunction7()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction9()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"
}
function myFunction9() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>How annoying.</i><br><br>&nbsp; Just shut up, Jenny. You're not my mom, for god's sake.<br><button onclick='myFunction8()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction10()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction10() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; I may not be your mom, but you're someone precious to me!<br>&nbsp; Come on, let's go! <br><button onclick='myFunction9()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction11()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"
}
function myFunction11() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>???Precious???<br>&nbsp; Whatever Jenny meant by that isn't important - she's dragged me to the nurse's office.<br>&nbsp; The nurse? <br>&nbsp; She isn't here.</i><br><button onclick='myFunction10()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction12a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://i.pinimg.com/474x/02/04/3d/02043d3e61dc5d31b7f102ea1db6f1b4.jpg' width='1300' height='1000'></p>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction12a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Hmm... the nurse isn't here...<br>&nbsp; Well I guess that's okay.<br>&nbsp; ???name???-kun, can you sit down on that bed for me?<button onclick='myFunction13a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"
}
function myFunction13a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Too lazy to even resist, I do as she says.<br>&nbsp; As though she's the nurse, Jenny patches up my scars 'n such.</i><br><button onclick='myFunction12a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction14a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction14a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; There...we...go! Okay, all done ???name???-kun.<br><button onclick='myFunction13a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction15a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"  
}
function myFunction15a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Thanks.<br><br>&nbsp; <i>I can only mumble. Jenny chuckles.</i><br><button onclick='myFunction14a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction16a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction16a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; No problem, ???name???-kun! You need to rely on me more. okay?<br><button onclick='myFunction15a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction17a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"  
}
function myFunction17a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ...K.<br><button onclick='myFunction16a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction18a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction18a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Shall we return to the classroom, then?<br><button onclick='myFunction17a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction19a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"  
}
function myFunction19a() {
  document.getElementById("myDIV1").innerHTML =  "";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunction20a()'><input type='submit' value='Back to the classroom'></p>"
}
function myFunction20a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>After 6 hours of boring and somewhat useless education, we finish our classes and get on our way <br>&nbsp; back home or to clubs. <br>&nbsp; I don't have CS Club today, so I begin packing to get home.</i><br><button onclick='myFunction19a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction21a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " ";  
  document.getElementById("myDIV4").innerHTML = "";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction21a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; H-hey, ???name???-kun!<br><button onclick='myFunction20a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction22a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny"  
}
function myFunction22a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Jenny. Again. Ugh.</i><br><br>&nbsp; Yea?<br><button onclick='myFunction21a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction23a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction23a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, umm... can we go home together today?<br><button onclick='myFunction22a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction24a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction24a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I can't really hide how surprised I am.<br>&nbsp; I hadn't expected that.</i><br><br>&nbsp; Ok, fine.<br><br>&nbsp; <i>Before I realized, I was giving her an okay, which surprised me again.</i><br><button onclick='myFunction23a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction25a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction25a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Really? Thank you! Then, let's go!<br><button onclick='myFunction24a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction26a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction26a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Jenny grabs my arm and pulls me down the stairs.</i><br><button onclick='myFunction25a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction27a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://aws1.discourse-cdn.com/pocketgems/uploads/episodeinteractive/original/3X/9/8/9859db3bc3ffbb3f0eb1b534889df1c48a14454a.jpeg' width='1300' height='auto'></p>";
}
function myFunction27a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Jenny, don't pull me, geez! <br><br>&nbsp; <i>The idiot isn't listening, laughing as she runs down the stairs like a little child.</i><br><button onclick='myFunction26a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction28a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction28a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>On the entire way home, Jenny was talking about what she had saw the other day, what she was talking <br>&nbsp; about with her friends, and other things I didn't really care about.<br>&nbsp; I just listened. I know Jenny's trying her best to make me feel more enthusiastic, but I'm never in the <br>&nbsp; mood for enthusiasm.</i><br><button onclick='myFunction27a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction29a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://i.pinimg.com/originals/5e/01/02/5e01028eceb0d3bc38631fa4b570f1bb.jpg' width='1300' height='1000'></p>";
}
function myFunction29a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ???name???-kun, I'm sorry.<br><button onclick='myFunction28a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction30a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction30a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ??? Why you apologizing?<br><button onclick='myFunction29a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction31a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction31a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, I've been the only one talking, and I know it must be boring to listen to someone like me <br>&nbsp; speak...<br><button onclick='myFunction30a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction32a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction32a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; You idiot. I never said that I find it boring, did it?<br>&nbsp; I enjoy listening to you talk; you're cute when you make your eyes sparkle as you explain everything.<br><button onclick='myFunction31a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction33a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction33a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ?!?!?!///// Tha-thanks, ???name???-kun, you're so nice...<br><button onclick='myFunction32a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction34a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction34a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>...........<br>&nbsp; ?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!<br>&nbsp; TF did I just say?!<br>&nbsp; You're cute as you speak?! Since when had I ever thought that?!<br>&nbsp; Did I just say that unconsciously? Does it mean that's how I actually think about Jenny?</i><br><br>&nbsp; J-Jenny! Forget what I just said right now!<br><button onclick='myFunction33a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction35a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction35a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Ehh~? I don't wanna!<br><button onclick='myFunction34a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction36a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction36a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Jenny runs away from me. Darn it, that brat.<br><br>&nbsp; Just as I was beginning to get lazy to chase after her, Jenny suddenly made a halt and turned back <br>&nbsp; at me.</i> <br><button onclick='myFunction35a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction37a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction37a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ???name???-kun. Let's return to school.<br><button onclick='myFunction36a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction38a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction38a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Go back? Why?</i><br><br>&nbsp; What? No, I don't want to. Did ya forget something?<br><button onclick='myFunction37a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction39a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction39a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; No.<br><button onclick='myFunction38a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction40a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction40a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Then, why?<br><br>&nbsp; H-hey, Jenny, wait-<br><br>&nbsp; <i>Before I get an answer, Jenny starts walking back in the direction we came from.<br>&nbsp; Does she really intend on going back?<br>&nbsp; What a pain... but Jenny looks like something's on her mind, so I guess I should follow her.</i><br><button onclick='myFunction39a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction41a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction41a() {
  document.getElementById("myDIV1").innerHTML =  ""
  document.getElementById("myDIV2").innerHTML =  
  "<p onclick='myFunction42a()'><input type='submit' value='Jenny looks like something is on her mind... walk with her back to school.'></p><br><br><p onclick='myFunction42b()'><input type='submit' value='Eh? Why tf should I? Too lazy to return. Turn your back on Jenny and walk in the direction towards home.'></p>";
}
function myFunction42a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Jenny, geez, just - just wait... <br><br>&nbsp; <i>The idiot just ran all the way back to school. <br>&nbsp; I'm out of breath.</i><br><button onclick='myFunction41a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction43a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML =  ""
  document.getElementById("name").innerHTML = "&nbsp; ??name???"
  document.getElementById("myDIV4").innerHTML = "<p><img src='http://www.mediafire.com/convkey/3ecb/8m9jq1euxxvza99zg.jpg?size_id=7' width='1300' height='1000'></p>"; 
}
function myFunction43a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ???name???-kun? Oh! Sorry...<br>&nbsp; I just ran off without you...<br><button onclick='myFunction42a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction44a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction44a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; It's alright, just... <br>&nbsp; Lemme catch my breath...<br>&nbsp; What happened? Why is coming back to school so urgent?<br><button onclick='myFunction43a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction45a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction45a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, that's because, umm...<br><button onclick='myFunction44a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction46a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny" 
}
function myFunction46a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>It's pretty late; no one's still in school.<br>&nbsp; If Jenny isn't speaking, my heavy breath is all I can hear. <br>&nbsp; I hear my heartbeat pounding on my chest.<br>&nbsp; Is it because I just ran all the way here, or is it for another reason...?</i><br><button onclick='myFunction45a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction47a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction47a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Awkward silence consumes time.<br>&nbsp; Jenny's blushing; I know it isn't because of the sunset.<br><br>&nbsp; I calmly, patiently wait for her to speak again.<br><button onclick='myFunction46a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction48a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction48a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ???name???-kun. Can we go to the rooftop?<br><button onclick='myFunction47a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction49a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny";
}
function myFunction49a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The roof?</i><br><br>&nbsp; Is it open? <br><button onclick='myFunction48a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction50a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???";
}
function myFunction50a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Jenny nods. <br><br>&nbsp; She walks back to me, takes my arm with her small hands, as always, and pulls me up the staircase.</i><br><button onclick='myFunction49a()' class='button2'><span>&nbsp;Previous</span></button><a href='jenny-happy.html'><button class='button'><span>Next&nbsp;</span></button></a>";
  document.getElementById("myDIV4").innerHTML = "<p><img src='https://media.moddb.com/images/members/4/3944/3943099/profile/hallway_evening.jpg' width='1300' height='1000'></p>"; 
}


function myFunction42b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Sorry kid, but I'm goin' home.<br><button onclick='myFunction41a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction43b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " "
}
function myFunction43b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Eh?...<br>&nbsp; Oh, okay...right...<br>&nbsp; You're busy, I know. Sorry ???name???-kun.<br><button onclick='myFunction42b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction44b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny "
}
function myFunction44b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I watch Jenny as she walks towards her own house.<br>&nbsp; Wasn't she going to school? Eh, doesn't matter.<br>&nbsp; After losing sight of Jenny's back, I walk back to my house.</i><br><button onclick='myFunction43b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction45b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name??? "
}
function myFunction45b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; *Sigh...* Well, I guess I'll have another chance to confess to ???name???-kun!<br>&nbsp; Yeah, can't get my hopes down!<br>&nbsp; I'll just tell him tomor--MMPF! MMMF! MMMMMMM!!!!!<br><button onclick='myFunction44b()' class='button2'><span>&nbsp;Previous</span></button><a href='jenny-bad.html'><button class='button'><span>Next&nbsp;</span></button></a>";
  document.getElementById("name").innerHTML = "&nbsp; Jenny "
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
