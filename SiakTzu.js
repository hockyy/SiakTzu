// ==UserScript==
// @id           SiakTzu
// @name         SiakTzu
// @namespace    http://tampermonkey.net/
// @version      1.0.0
// @description  This userscript lets you win SiakWar
// @author       hockyy
// @match        https://academic.ui.ac.id/main/Schedule/Index?period=*&search=
// ==/UserScript==

var matkul_code = ["620020-4","620207-4","620077-3","620137-3","620289-3","620173-6"]
var matkul_len = matkul_code.length;
var i,j,cnt,now,tmp
(function() {
    cnt = 0;
    console.log('Matkul picked :')
    for(i = 0;i < matkul_len;i++){
        console.log(matkul_code[i])
    }
    console.log(matkul_len)
    for (i = 0;i <= 500;i++){
        now = 'c'+i.toString()
        // console.log(now)
        if(document.getElementById(now) == null) continue;
        console.log(now+' exists')
        for(j = 0;j < matkul_len;j++){
            if(document.getElementById(now).value != matkul_code[j]) continue;
            console.log("Found ! " + matkul_code[j] + " " + now)
            cnt++
            if(document.getElementById(now).checked != true){
                console.log("Clicking !");
                document.getElementById(now).click();
            }
            else {
                console.log("Already selected!");
            }
            break;
        }
    }
    var scrollingElement = (document.scrollingElement || document.body);
    scrollingElement.scrollTop = scrollingElement.scrollHeight;
    alert("Is Done! Checked "+cnt);
})();