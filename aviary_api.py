#!/usr/bin/python
################################################################################
# Method that takes image and returns code for Aviary embed

def aviary_embed(imageURL, linkText):
    output = "<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js\" type=\"text/javascript\"></script>\n"
    output += "<script>var AviaryJS = AviaryJS || {};AviaryJS.isLoggedIn = false;</script>\n"
    output += "<script type=\"text/javascript\" src=\"static/js/aviary.js\"></script>\n"
    output += "<script>var img = document.createElement(\"img\");img.setAttribute(\"src\", \""+imageURL+");"
    output += "img.setAttribute(\"id\", \"feather_demo\"); img.setAttribute(\"style\", \"display:none\");document.body.appendChild(img);</script>\n"
    output += "<a href=\"#\" onclick=\"return AviaryJS.showFeather();\" class=\"action_button\">"+linkText+"</a>";
    return output
