# CTFd Theme Development Plan: mcsc

## Goal
Create a new CTFd theme named "mcsc" with a "purple, dark blue, cyberpunk themed, console/terminal looking UI."

## Plan Steps

1.  **Create Theme Directory Structure:**
    *   **Description:** Create the necessary directory structure for the new `mcsc` theme under `CTFd/themes/`. This will include `assets/`, `static/`, and `templates/` subdirectories, mirroring the standard CTFd theme layout.
    *   **Details:**
        *   `CTFd/themes/mcsc/`
        *   `CTFd/themes/mcsc/assets/`
        *   `CTFd/themes/mcsc/static/`
        *   `CTFd/themes/mcsc/templates/`

2.  **Copy Base Files:**
    *   **Description:** Copy essential base files from the `core` theme to the new `mcsc` theme to establish a working foundation.
    *   **Details:**
        *   Copy `CTFd/themes/core/templates/base.html` to `CTFd/themes/mcsc/templates/base.html`.
        *   Copy the entire `CTFd/themes/core/static/css/` directory to `CTFd/themes/mcsc/static/css/`.

3.  **Modify CSS for Theme:**
    *   **Description:** Update the CSS files in the `mcsc/static/css/` directory to implement the desired visual theme (purple, dark blue, cyberpunk, console/terminal).
    *   **Details:** This will involve:
        *   Adjusting color variables for backgrounds, text, accents, and links.
        *   Selecting appropriate fonts for a console/terminal look.
        *   Modifying component styles (buttons, forms, navigation) to fit the cyberpunk aesthetic.
        *   Potentially adding subtle animations or effects to enhance the UI.

4.  **Review and Refine:**
    *   **Description:** After initial implementation, review the theme's appearance and make necessary adjustments based on feedback.
    *   **Details:**
        *   Provide instructions on how to enable and run CTFd with the new `mcsc` theme.
        *   Collaborate on visual feedback and iterative improvements.

## Next Steps

I will now proceed with creating the directory structure and copying the base files.
