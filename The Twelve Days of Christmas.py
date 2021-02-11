def f():
   w=''
   for k in range(12):w+='On the %s day of Christmas\nMy true love sent to me'%'First^Second^Third^Fourth^Fifth^Sixth^Seventh^Eighth^Ninth^Tenth^Eleventh^Twelfth'.split('^')[k]+'\n';w=w+'\n'.join('Twelve drummers drumm*Eleven pipers pip*Ten lords a-leap*Nine ladies danc*Eight maids a-milk*Seven swans a-swimm*Six geese a-lay*Five gold rings,^Four calling birds,^Three French hens,^Two turtle doves, and^A partridge in a pear tree.\n^'.replace('*','ing,^').split('^')[11-k:])
   return w[:-2}