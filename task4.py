good = r"""
        (,        ,)
        |  *_      |
        \\ (('^,  //
         \`()) _.'/
          ` )__)-'
            \  )
             )(
            /  `_.'_
           /   /_ , )
          /_.-'  ( /
            \ |  ,/
             \'( /
             ),)/
            ( )`
             \
             , 
 ejm         '|
             \/
             """
bad = r"""
             .  .
             |\_|\
             | a_a\
             | | "]
         ____| '-\___
        /.----.___.-'\
       //        _    \
      //   .-. (~v~) /|
     |'|  /\:  .--  / \
    // |-/  \_/____/\/~|
   |/  \ |  []_|_|_] \ |
   | \  | \ |___   _\ ]_}
   | |  '-' /   '.'  |
   | |     /    /|:  |
   | |     |   / |:  /\
   | |     /  /  |  /  \
   | |    |  /  /  |    \
   \ |    |/\/  |/|/\    \
    \|\ |\|  |  | / /\/\__\
     \ \| | /   | |__
   snd    / |   |____)
          |_/
        """
drawbridge_raised = True
if not drawbridge_raised:
    outcome = "Thunder: Let's get out of here!"
    print(good)
else:
    outcome = "Doom: How, theres no way!"
    print(bad)
print(outcome)