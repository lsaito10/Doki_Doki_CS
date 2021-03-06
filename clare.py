#!/usr/bin/python3

print ('Content-type: text/html\n')

Template = '''
<!DOCTYPE html>
<html>
<title>Clare</title>
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
        background-image: url("clare1.jpeg");
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
  "&nbsp; One day, I was walking home, when a sudden flash of light surrounded me.<button onclick='myFunction0()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV3").innerHTML = " ";
}
function myFunction0() {
  document.getElementById("myDIV1").innerHTML =  "	";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunctiona()'><input type='submit' value='WTF?!'></p>"
}
function myFunctiona() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; <i>As the sudden flash of light surrounded me, I closed my eyes tight shut.<br>&nbsp; The next moment, when I opened my eyes, a girl was standing in front of me.<br><button onclick='myFunction()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunctionb()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " ";
  document.getElementById("myDIV3").innerHTML = "<img src='http://www.seekgif.com/uploads/sparkle-transparent-png-background-3.png' width='500' height='550'>";
}
function myFunctionb() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; .....<br><button onclick='myFunctiona()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction1()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV3").innerHTML = "<img src='clare.png' width='500' height='550'>";
  document.getElementById("name").innerHTML = "&nbsp; ??? ";
}
function myFunction1() {
  document.getElementById("myDIV1").innerHTML = 
  "&nbsp; Wh-Who are you?!<br><button onclick='myFunctionb()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction2()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction2() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; ........... <br><button onclick='myFunction1()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction3()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???"
}
function myFunction3() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; ...........H-Hello?...... <br><button onclick='myFunction2()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction4()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction4() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; ....Umm, are you okay? <br><button onclick='myFunction3()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction5()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV3").innerHTML = "<img src='clare.png' width='500' height='550'>";
}
function myFunction5() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; <i>I tried to ask for her name, when suddenly, she comes straight up to me and stares straight at my <br>&nbsp; face.</i> <br><button onclick='myFunction4()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction6()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV3").innerHTML = "<img src='clareface.png' width='960' height='750'>";
}
function myFunction6() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; ?!?!?!?!?!?!?! <br><button onclick='myFunction5()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction7()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction7() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I jump back, afraid she'll do something to me.<br>&nbsp; She doesn't try to get any closer. Good; maybe she doesn't mean any harm. <br>&nbsp; Getting a good look at her face, I see that her skin isn't human-colored.<br>&nbsp; It's dark out, and a bit hard to see - but... her skin's pink.</i><br><button onclick='myFunction6()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction8()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction8() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; P-pink? <br><button onclick='myFunction7()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction9()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction9() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; Hungry...food...food... <br><button onclick='myFunction8()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction10()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???"
}
function myFunction10() {
  document.getElementById("myDIV1").innerHTML =  "&nbsp; <i>Is she hungry?</i> <br><button onclick='myFunction9()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction11()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"
}
function myFunction11() {
  document.getElementById("myDIV1").innerHTML =  "	";
  document.getElementById("myDIV2").innerHTML = "<p onclick='myFunction12a()'><input type='submit' value='Give her that sandwich that was in your backpack.'></p><br><br><p onclick='myFunction12b()'><input type='submit' value='Why should I care?'></p>"
}
function myFunction12a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; H-Here's a sandwich!<br><br>&nbsp;<i> I was waiting to eat that sandwich once I'd gotten home, but she looks like she's pretty hungry, so <br>&nbsp; might as well be nice.</i><button onclick='myFunction13a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " "
}
function myFunction13a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ...?...San..d...wich?<br><button onclick='myFunction12a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction14a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???"  
}
function myFunction14a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The girl looks at the sandwich, then back at me. She's tilting her head, looking confused.<br>&nbsp; Does she not know what a sandwich is?</i><br><button onclick='myFunction13a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction15a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction15a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Uhh... It's food. Good food, made of bread and ham and... that's not important. Just try it out. <br>&nbsp; You're hungry, aren't you?<br><button onclick='myFunction14a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction16a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction16a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The girl nods, then points at the sandwich.</i><br><button onclick='myFunction15a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction17a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction17a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Good food?<br><button onclick='myFunction16a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction18a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???"  
}
function myFunction18a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I nod, indicating yes.<br>&nbsp; The next moment, the girl's eyes sparkle, and a trickle of drool goes down her mouth.<br>&nbsp; She grabs the sandwich out of my hand and stuffs it into her mouth. </i><br><button onclick='myFunction17a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction19a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???"  
}
function myFunction19a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Like a chipmunk, her mouth is full with the sandwich. I ask her if it tastes good. Squinting her eyes <br>&nbsp; and seeming as though she's eating the best tasting food in the world, she smiles, nodding yes.<br>&nbsp; I've got to admit; that was cute.</i><br><button onclick='myFunction18a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction20a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction20a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>She's humming now, a tune I've never heard, while swinging her feet back and forth.<br>&nbsp; That's when I realized: she's floating. No wonder she can swing her feet when she's standing.<br>&nbsp; Fear comes up again, as now it's clear that she isn't a human; but how can such a cute creature mean <br>&nbsp; any harm?</i><br><button onclick='myFunction19a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction21a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction21a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The girl finishes eating. I gather up my courage and ask:</i><br><br>&nbsp; So, what's your name?<br><button onclick='myFunction20a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction22a()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction22a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; My name...?<br><button onclick='myFunction21a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction23a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???" 
}
function myFunction23a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I nod.</i><br><br>&nbsp; Yeah, your name. And also where you're from., if you don't mind.<br><br>&nbsp; <i>She looks really young; much younger than me. Even if she isn't a human, her parents are probably <br>&nbsp; worrying about her.<br>&nbsp; She takes a deep breath in, and opens up her mouth.</i><br><button onclick='myFunction22a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction24a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction24a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; I am Clare. Clare von Eisenburg. I'm the queen of the Eisenburg kingdom, in another dimension.<br><button onclick='myFunction23a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction25a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction25a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>A queen...? No way. She's gotta be kidding.<br>&nbsp; That's right; this whole encounter with Clare must be a joke. Yeah.</i><br><button onclick='myFunction24a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction26a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction26a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; You must be thinking I'm joking, aren't you?<br><button onclick='myFunction25a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction27a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction27a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>?!?!?!?!??!<br>&nbsp; How in the world's she know? What?!</i>  <br><button onclick='myFunction26a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction28a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction28a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Fufufu... Looks like I'm right, no?  <br><button onclick='myFunction27a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction29a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction29a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I nod, completely surprised.</i><br><br>&nbsp; Alright, Clare. I believe you. But what's a queen doing here?<br><button onclick='myFunction28a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction30a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction30a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, I got tired of being stuck in my world, so I tried running away...<br><button onclick='myFunction29a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction31a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction31a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Can a queen be so irresponsible?</i><br><button onclick='myFunction30a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction32a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction32a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ...But then, I got lost, and I was walking around for a pretty long time.<br>&nbsp; And when I was on the verge of collapsing from hunger, you appeared in front of me, and gave me <br>&nbsp; food. <br>&nbsp; If you hadn't given me anything, I might've killed you.<br><button onclick='myFunction31a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction33a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction33a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Wow, wow, wow... hold up. <br>&nbsp; You're saying that you would've killed me if I didn't give you any food? <br>&nbsp; What if I didn't have anything on me?!<br><button onclick='myFunction32a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction34a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction34a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Well, yeah, I would've killed you. Hunger's more important.<br>&nbsp; You had good luck there, friend.<br>&nbsp; Oh yeah, what's your name? I forgot to ask.<br><button onclick='myFunction33a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction35a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction35a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Geez, this person's smiling as she's saying something terrible...</i><br><br>&nbsp; My name's ???name???.<br><button onclick='myFunction34a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction36a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction36a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; ???name???, huh? <br>&nbsp; That's a nice name you've got there.<br>&nbsp; First off, thank you for saving me.<br><button onclick='myFunction35a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction37a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction37a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Clare takes an elegant bow, suddenly making the fact that she's a queen of another dimension more <br>&nbsp; realistic.</i><br><button onclick='myFunction36a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction38a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction38a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Second off, ???name???, I have a request to make.<br><button onclick='myFunction37a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction39a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction39a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>A request?</i><br><br>&nbsp; Sure, what is it?<br><button onclick='myFunction38a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction40a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction40a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Will you, well... marry me?//<br><button onclick='myFunction39a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction41a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction41a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>...<br>&nbsp; ...???<br>&nbsp; ?!?!?!??!?!?!?!</i><br><br>&nbsp; Wha-WHAT?! Marry you?!<br>&nbsp; Hold up, Clare, we've only just met and... first off, I'm a normal human; I'm just a high-schooler! <br>&nbsp; And---<br><button onclick='myFunction40a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction42a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction42a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; You have no right to refuse.<br>&nbsp; I'm the queen of the Eisenburg Kingdom. What I say becomes definite. <br>&nbsp; You're coming with me.<br><button onclick='myFunction41a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction43a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction43a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Clare, wait! I'm not into lolis!!!<br><button onclick='myFunction42a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction44a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction44a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; I am NOT a loli!<br>&nbsp; Plus, you must be the destined one for me!<br>&nbsp; Honey, we're going to my dimension!<br>&nbsp; If you refuse, you DIE!<br><button onclick='myFunction43a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction45a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; Clare" 
}
function myFunction45a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Wha---<br><button onclick='myFunction44a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction46a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction46a() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>The next moment, another flash of light surrounded me.</i><br><button onclick='myFunction45a()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction47a()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("name").innerHTML = "&nbsp; ???name???" 
}
function myFunction47a() {
  document.getElementById("myDIV1").innerHTML =  " ";
  document.getElementById("name").innerHTML = " ";
  document.getElementById("myDIV2").innerHTML =  "<a href='clare-happy.html'><input type='submit' value='Several years later...'></a>";
  document.getElementById("myDIV3").innerHTML =  "<img src='http://www.seekgif.com/uploads/sparkle-transparent-png-background-3.png' width='500' height='550'> ";
}

function myFunction12b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; Um... Sorry, I'm kinda in a hurry. Bye!<br><br>&nbsp; <i>Better off not to get close to people like her. Run away!</i><br><button onclick='myFunction11()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction13b()' class='button'><span>Next&nbsp;</span></button>";
  document.getElementById("myDIV2").innerHTML = " "
}
function myFunction13b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>I begin running away.<br>&nbsp; Honestly speaking, I had a sandwich in my bag, but I want to eat it.</i><br><button onclick='myFunction12b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction14b()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction14b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>Just as I was about to turn at the corner and finally be in a 50m distance from my home, someone <br>&nbsp; grabbed my shoulder.</i><br><button onclick='myFunction13b()' class='button2'><span>&nbsp;Previous</span></button><button onclick='myFunction15b()' class='button'><span>Next&nbsp;</span></button>";
}
function myFunction15b() {
  document.getElementById("myDIV1").innerHTML =  
  "&nbsp; <i>*Thump*</i><br><button onclick='myFunction14b()' class='button2'><span>&nbsp;Previous</span></button><a href='clare-bad.html'><button class='button'><span>Next&nbsp;</span></button></a>";
  document.getElementById("myDIV3").innerHTML = "<img src='clareface.png' width='960' height='750'>";
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
