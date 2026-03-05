good = r"""
                   _..
  /}_{\           /.-'
 ( a a )-.___...-'/
 ==._.==         ;
      \ i _..._ /,
      {_;/   {_//  fsc
        """
bad = r"""
     .-._______
  .={ . }..--""
 [/"`._.'    fsc
        """
torch_lit = False
if torch_lit:
    outcome = "Flicker: Wow, light!!"
    print(good)
else:
    outcome = "Doom: Who turned off the lights?"
    print(bad)
print(outcome)