# SiakTzu by Hocky Yudhiono


SiakWar + Sun Tzu ez ez


- Login with your UI Account https://academic.ui.ac.id/main/Authentication/
- Put your `classcode-credit` (grab from : https://academic.ui.ac.id/main/Schedule/Index)
- ![image-20220115133402225](README.assets/image-20220115133402225.png)
- For example, this is `658875-3`

## Selenium Automated Bot (Bot)

- Fill username and password
- ![image-20220115133715642](README.assets/image-20220115133715642.png)
- Update `matkul_code` dictionary, value is not important, key is `classcode-credit`
- ![image-20220115133320500](README.assets/image-20220115133320500.png)
- Run `python SiakTzu.py` in cmd

## JS Version (Injects Scripts Using Chrome)

Example of use :


- Install [tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=id), Add the script, by pressing `Create a new script...`
- ![image-20220115132840341](README.assets/image-20220115132840341.png)
- Paste [SiakTzu.js](./SiakTzu.js)
- get to this (https://academic.ui.ac.id/main/CoursePlan/CoursePlanEdit) when you can Add your IRS
- It will automatically check and submit.
- Win The War !
- ![image-20220115133016163](README.assets/image-20220115133016163.png)



