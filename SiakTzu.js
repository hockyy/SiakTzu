// ==UserScript==
// @id           SiakTzu
// @name         SiakTzu
// @namespace    http://tampermonkey.net/
// @version      1.1.0
// @description  This userscript lets you win SiakWar
// @author       hockyy
// @match        https://academic.ui.ac.id/main/CoursePlan/CoursePlanEdit
// ==/UserScript==

(function() {
    var i, j, now;
    var matkul_code = ["696009-3", "695927-3", "695972-4", "695926-3"]
    var matkul_len = matkul_code.length;
    var cnt = 0;
    console.log('Matkul picked :')
    for(i = 0;i < matkul_len;i++){
        console.log(matkul_code[i])
    }
    console.log(matkul_len)
    for (i = 0;i <= 800;i++){
        now = 'c'+i.toString();
        // console.log(now)
        if(document.getElementById(now) == null) continue;
        console.log(now+' exists');
        for(j = 0;j < matkul_len;j++){
            if(document.getElementById(now).value != matkul_code[j]) continue;
            console.log("Found ! " + matkul_code[j] + " " + now);
            cnt++
            console.log("Clicking !");
            if(!document.getElementById(now).checked){
                document.getElementById(now).click();
            }
            break;
        }
    }
    var scrollingElement = (document.scrollingElement || document.body);
    scrollingElement.scrollTop = scrollingElement.scrollHeight;
    alert("Is Done! Checked "+cnt);
})();