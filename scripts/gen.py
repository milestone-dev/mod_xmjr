import sys
val = sys.argv[1]
dbg = True
waves = 25
if val == "w":
	for i in range(1, waves):
		print('\
		{{"classname" "trigger_relay" "targetname" "wave" "target" "w{0}_exec" "message" "{3}" }}\n\
		{{"classname" "trigger_relay" "targetname" "w{0}_exec" "message" "{4}" "target2" "w{0}_done" "spawnflags" "32" "target" "w{0}_setup" "delay" "0.2" }}\n\
		{{"classname" "trigger_entitystate_off" "targetname" "w{0}_done" "target" "w{0}_exec" }}\n\
		{{"classname" "trigger_entitystate_on" "targetname" "w{1}_done" "target" "w{0}_exec" }}\n\
		{{"classname" "trigger_monsterkill" "targetname" "w{0}_setup" "target" "w{1}_setup" }}\n\
		'.format(i, i - 1, i + 1, "w"+str(i) if dbg else "", "w"+str(i)+"_exec!" if dbg else ""))
		print("\n")
else:
	for i in range(1, waves):
		print ('{{"classname" "monster_{1}" "targetname" "w{0}_setup" "spawnflags" "112" "nomonstercount" "1" }}'.format(i, val))