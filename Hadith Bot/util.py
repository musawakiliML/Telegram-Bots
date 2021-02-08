def pattern(value):
    patterns = ['<p>', '</p>','<b>','</b>', '<br/>','<i>','</i>']

    for i in patterns:
        if i in value:
            value = value.replace(i,'')
    return value

    #if '<p>' in value:
        #return value.replace("<p>","")
#test_string = "man<p>jf</p>vchg<b>hg</b>ggh<br/>hfgf<i>bfh</i>"

#test_value = test_pattern(test_string)

#print(test_value)