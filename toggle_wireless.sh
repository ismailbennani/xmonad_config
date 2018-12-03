STATUS=$(nmcli radio wifi)

if [ $STATUS = "disabled" ]; then
  echo "Wifi enabled"
  nmcli radio wifi on
else
  echo "Wifi disabled"
  nmcli radio wifi off
fi;
