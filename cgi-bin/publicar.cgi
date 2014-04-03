#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Form Example</title>'
echo '</head>'
echo '<body>'

	/usr/bin/env | grep "REMOTE_ADDR"
echo "<form method=\"POST\"  action=\"\">"
echo '<table nowrap><tr><td>Titulo</TD><TD><input type="text" name="val_x" size=100></td></tr><tr><td>Comentario</td><td><input type="text" name="val_y" size=100 value=""></td></tr></table><br><input type="submit" value="Process Form"><input type="reset" value="Reset"></form>'

  # Make sure we have been invoked properly.

  if [ "$REQUEST_METHOD" != "POST" ]; then
        echo "<hr>Script Error:"\
             "<br>Usage error, cannot complete request, REQUEST_METHOD!=POST."\
             "<br>Check your FORM declaration and be sure to use METHOD=\"POST\".<hr>"
        exit 1
  fi

  # If no search arguments, exit gracefully now.

#  if [ ! -z "$QUERY_STRING" ]; then
     # No looping this time, just extract the data you are looking for with sed:
     XX=`echo "$QUERY_STRING" | sed -n 's/^.*val_x=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     YY=`echo "$QUERY_STRING" | sed -n 's/^.*val_y=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`

     echo "$XX" | /usr/local/bin/ciboulette -a "$YY" 2> /dev/null 1> /dev/null
#  fi
echo '</body>'
echo '</html>'

exit 0

