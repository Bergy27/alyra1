function estPalindrome(str) {
    str = str.replace( /\s/g, '');
    var rts = str.split("").reverse().join("");
    return(str==rts)
}

console.log(estPalindrome("ESOPE RESTE ICI ET SE REPOSE"));
console.log(estPalindrome("ASSIETTE"));
