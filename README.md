🔢 Number Guessing Game
================================

Overview
--------

A simple yet engaging number guessing game built with Python and Streamlit. Test your intuition by guessing the number the computer has chosen across three difficulty levels!

Features
--------

*   **Three Difficulty Levels**:
    
    *   Easy (1-50 numbers)
        
    *   Medium (1-100 numbers)
        
    *   Hard (1-200 numbers)
        
*   **Score Tracking**: Keeps count of your correct guesses
    
*   **Attempt Counter**: Tracks total number of guesses
    
*   **Instant Feedback**: Tells you whether your guess was higher or lower than the target
    
*   **Responsive UI**: Clean interface built with Streamlit
    

How to Play
-----------

1.  Select your preferred difficulty level
    
2.  Enter your guess in the number input field
    
3.  Click "Submit" to see if you guessed correctly
    
4.  The game will tell you if your guess was higher or lower than the target number
    
5.  When you guess correctly, your score increases!
    
6.  The game tracks your total attempts across sessions
    

Installation
------------

1.  bashCopyDownloadgit clone https://github.com/your-username/number-guessing-game.git
    
2.  bashCopyDownloadpip install streamlit
    

Running the Game
----------------

bashCopyDownload

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

Requirements
------------

*   Python 3.x
    
*   Streamlit
    
*   Random (built-in Python module)
    

Game Logic
----------

*   The computer randomly selects a number within the chosen difficulty range
    
*   You win when your guess matches the computer's number
    
*   Your score increases by 1 with each correct guess
    
*   The game tracks your total attempts regardless of correct/incorrect guesses