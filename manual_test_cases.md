# manual test cases - contact book
## TC_01 : Add a contact from the menu (positive)
**precondition**  the program is running in the terminal
**steps of the test** 
1-choose option add and press enter 
2-add a name and a number 
3-select back step
**expected result**  save the contact successfully 
**actual resulet**  it did save the contact !
**status** PASS
## TC_02 : try a wrong input like enter a wrong spell of add in the menu  (negative)
**precondition**  the program is running in the terminal
**steps of the test** 
1-choose option from the menu by typing a wrong spell like ad and press enter 
**expected result** gives you a friendly massage means you should choose between add , show all , exit  
**actual result**  it ptint us the massage we expected 
**status** PASS
## TC_03 : try  a wrong input like a number in the menu (negative)
**precondition**  the program is running in the terminal
**steps of the test** 
1-enter a number inside the choose option 
**expected result**  the program gives us a massage says that you enterd a number please enter a text and choose between add , show all , exit  
**actual result**  it did said that we enterd a wrong choice and printed us saying to choose between the options we already see in the menu 
**status** PASS
## TC_04 : try to enter an empty massage at the menu (negative)
**precondition**  the program is running in the terminal
**steps of the test** 
1-press enter without typing
2-get the menu again then press space and enter after it 
**expected result** it should show us a freindly massage says we enterd a wrong choice please choose between add , show all , exit  
**actual result**  it worked as expected result
**status** PASS
## TC_05 try the show all option (positive)
**precondition**  the program is running in the terminal
**steps of the test** 
1-enter show all in the menu options
 
**expected result** it should show us the all contacts we added and back to the menu 
**actual result**  it worked as expected result
**status** PASS
## TC_06 test the exit option (positive)
**precondition**  the program is running in the terminal
**steps of the test** 
1-enter exit in the menu options
**expected result** it should print us a nice massage to goodbye the user and stop working
**actual result**  it worked as expected result
**status**PASS

# bugs 
there is no bugs in this test run.
