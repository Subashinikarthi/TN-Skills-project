async function generateComic() {

    const storyPrompt =
        document
            .getElementById(
                "storyPrompt"
            )
            .value
            .trim();


    const characterName =
        document
            .getElementById(
                "characterName"
            )
            .value
            .trim();


    const setting =
        document
            .getElementById(
                "setting"
            )
            .value
            .trim();


    const tone =
        document
            .getElementById(
                "tone"
            )
            .value;


    const artStyle =
        document
            .getElementById(
                "artStyle"
            )
            .value;


    const loading =
        document.getElementById(
            "loading"
        );


    const errorMessage =
        document.getElementById(
            "errorMessage"
        );


    const button =
        document.getElementById(
            "generateButton"
        );


    if (!storyPrompt) {

        errorMessage.textContent =
            "Please enter a story idea.";

        return;

    }


    errorMessage.textContent =
        "";


    loading.classList.remove(
        "hidden"
    );


    button.disabled = true;


    try {

        const response =
            await fetch(
                "/generate-comic/json",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        story_prompt:
                            storyPrompt,

                        character_name:
                            characterName
                            || "Alex",

                        setting:
                            setting
                            || "Modern city",

                        tone:
                            tone,

                        art_style:
                            artStyle

                    })

                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail
                || "Comic generation failed."
            );

        }


        sessionStorage.setItem(
            "comic",
            JSON.stringify(data)
        );


        window.location.href =
            "/comic-preview";

    }
    catch (error) {

        errorMessage.textContent =
            error.message;

    }
    finally {

        loading.classList.add(
            "hidden"
        );

        button.disabled = false;

    }

}