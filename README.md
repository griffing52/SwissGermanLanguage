# SwissGermanLanguage

The project is designed to assist with learning Swiss German by creating lesson audio files that integrate pronunciation and translations. The program organizes lessons based on complexity and repetition frequency, enhancing the learning experience through gradual exposure and spaced repetition.

### Key Features

1.  **Dynamic Audio Generation**: The project creates Swiss German phrases and corresponding translations using `mp3` files, which are compiled into lessons.
2.  **Complexity-Based Spacing**: Words and phrases are chosen based on their repetition frequency, and "old" words are revisited after a certain threshold.
3.  **Silent Pauses**: Silence intervals vary based on complexity, allowing for mental processing time between new and familiar phrases.
4.  **Lesson Compilation**: Lessons are organized by reading input files, converting them into phrases and comments, and exporting the final audio file for a chapter.

### Requirements

-   **Python**: Base environment.
-   **pydub**: For audio manipulation.
-   **Text-to-Speech Service**: Utilized for creating audio translations.
-   **mp3 Audio Files**: Used for words and phrases.


### Input File Structure

- $ = inject mp3
- | = define word/phrase
- \# = inject comment
- / or nothing = ignore line
- \* = important phrase

#### Example
```bash
#you will learn how to have this conversation with someone! Just listen now, and everything will be explained later! 
$conversation1
|mier gond=we are going
|mier gond uf Italie=we are going to Italy
|mier hend luscht=we want to
|mier gond das wuchenendi uf Italie=we are going to Italy this weekend
```

Explanation of Core Functions
-----------------------------

### `compile`

This function reads the lesson data from input text files and builds an audio structure for a lesson.

-   **Word Dictionary**: Stores words with their English translations.
-   **Phrase Parsing**: Identifies Swiss German phrases and their translations, converting them into `mp3` files.
-   **Dependencies and Spacing**: Phrases are chosen based on dependencies. Older phrases (age > `OLD_AGE`) are revisited for spaced repetition.

### `build`

This function combines all audio segments into a single `mp3` file.

-   **Silence Management**: Injects silence intervals based on the complexity level, helping with mental processing.
-   **Final Audio Composition**: Joins each audio segment into the complete lesson audio, which is then exported as an `mp3`.

### `writeWordAudioSegment`

Generates and writes an audio segment for each word or phrase:

-   **Repetition Increment**: Tracks how often a word or phrase is used.
-   **Random Intros and Starters**: Randomly selects an introduction or prompt before each new word, adding variability.

Lesson Organization Algorithm
-----------------------------

The project's algorithm uses a complexity-based approach with spaced repetition to determine how frequently each word or phrase is revisited in the lesson. Here's a flowchart illustrating the lesson structure and the algorithm's flow:

plaintext

Copy code

`+-------------------------------------------------+
| Start                                           |
+-------------------------------------------------+
            |
            v
+-----------+---------------------------+
| 1. Initialize time, wordDict, phrases|
+--------------------------------------+
            |
            v
+-----------+---------------------------+
| 2. Read words and phrases             |
| - Identify each word, phrase          |
| - Translate and save as mp3           |
+--------------------------------------+
            |
            v
+-----------+---------------------------+
| 3. Inject Phrases Based on Rules      |
| - If complex phrase: Add dependencies|
| - Else: Add to order list            |
+--------------------------------------+
            |
            v
+-----------+---------------------------+
| 4. Compile Lesson Order              |
| - Add silent pauses per complexity   |
| - Select intros randomly             |
| - Update time for each repetition    |
+--------------------------------------+
            |
            v
+-----------+---------------------------+
| 5. Generate Final Audio              |
| - Join each mp3 into a complete file |
| - Export as mp3 for the lesson       |
+--------------------------------------+
            |
            v
+-----------+---------------------------+
| End                                   |
+--------------------------------------+`

This design allows for customized lesson flows where high-frequency phrases are repeated less often while less familiar ones are revisited. This spaced repetition methodology ensures that learners are continuously exposed to newer words and phrases while retaining previously learned material.

Usage Example
-------------

1.  **Prepare Input Files**: Create `words.txt` and `lessons.txt` with Swiss German phrases and English translations.
2.  **Compile the Lesson**: Run the `compile()` function with the lesson file to parse and order phrases.
3.  **Build the Lesson Audio**: Call `build()` to generate the lesson's final audio file.
4.  **Clean Up**: Use `clean()` to delete intermediate audio files once the final audio is complete.

### Potential Improvements

-   **Interactive Audio Feedback**: Enable learners to record and playback their pronunciations.
-   **Customized Complexity Levels**: Allow users to select difficulty levels for tailored lesson content.
-   **Mobile Compatibility**: Adapt for mobile use to provide on-the-go practice sessions.

This project is a dynamic tool for learning Swiss German, leveraging a sophisticated algorithm to optimize the learning process through auditory engagement and repetition.
