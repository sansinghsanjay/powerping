1. All Python imports must be preceded by the comment `# Python imports` without any blank-line gaps.
2. All project imports must be preceded by a comment using the first-level directory name, such as `# Util imports` or `# Module imports` without any blank-line gaps.
3. Every function must include a clean, easy-to-read multi-line comment immediately below the function definition, describing its purpose, argument details, and return values with proper line breaks and indentation.
4. Every endpoint must return a JSON object with the following required fields: `"status"` (allowed values: `"success"` or `"fail"`) and `"message"` (a short human-readable description of the outcome, such as a success confirmation or failure reason). The response may also include the optional field `"data"`, which contains the main payload returned by the endpoint.
5. There must be a gap of two blank lines between functions.
6. A dedicated logging function must be used to record progress. The function must accept the following arguments:
    i. Status: `info`, `error`, `warning`, or `debug`
    ii. Filename: Name of the file from which the logging function is called
    iii. Function name: Name of the function that calls the logging function
    iv. Message: Logging message in lowercase
   In addition to the above arguments, the logging function must prepend a timestamp.
7. Outside function bodies, keep exactly two blank lines between consecutive code sections (for example, between import blocks, configuration/setup blocks, and endpoint declarations).
8. All classes must include a docstring immediately below the class declaration that briefly describes the purpose and responsibility of the class. The docstring should clearly explain what the class represents or does, not how it works internally.
9. Each logical section or group of related lines of code that work together to accomplish a specific task should include a clear comment explaining the purpose of that block. The comment should describe what the block of code is intended to achieve, helping readers quickly understand the intent without needing to analyze every line.
10. A corresponding test must be added under the `tests` directory for every function/file wherever testing is required and reasonably possible (for example: unit tests for pure logic, integration tests for API/database behavior, and negative-path tests for validation/error handling).