function showFlashMessage(message, bg_color, color, duration) {
    // Create message element
    let flashMessage = document.createElement('div');
    flashMessage.textContent = message;
    flashMessage.style.backgroundColor = bg_color;
    flashMessage.style.color = color
    flashMessage.classList.add('flash-message');

    // Append message to the container
    document.body.appendChild(flashMessage);

    // Set timeout to remove message
    setTimeout(function () {
        flashMessage.remove();
    }, duration);
}

function searchDiaryEntries() {
    let input = document.getElementById('search').value.toLowerCase();
    let diaryEntries = document.querySelectorAll('.diary-entry');

    // Hide text input, tag input, and add button initially
    document.getElementById('diary-text').classList.add('hidden');
    document.getElementById('tag-input').classList.add('hidden');
    document.getElementById('add-button').classList.add('hidden');

    diaryEntries.forEach(entry => {
        let memoElement = entry.querySelector('.memo');
        let tagElement = entry.querySelector('.tag');
        let memo = memoElement.textContent.toLowerCase();
        let tag = tagElement.textContent.toLowerCase();

        if (memo.includes(input) || tag.includes(input)) {
            entry.style.display = 'block'; // Show the diary entry

            // Highlight the matching parts
            if (memo.includes(input)) {
                // Highlight memo
                memoElement.innerHTML = memo.replace(new RegExp(input, 'gi'), match => `<span class="highlight">${match}</span>`);
            }
            if (tag.includes(input)) {
                // Highlight tag
                tagElement.innerHTML = tag.replace(new RegExp(input, 'gi'), match => `<span class="highlight">${match}</span>`);
            }
        } else {
            entry.style.display = 'none'; // Hide the diary entry
        }
    });


}

function addDiaryEntry() {
    let diaryText = document.getElementById('diary-text').value;
    let tagInput = document.getElementById('tag-input').value;

    // Clear the fields
    document.getElementById('diary-text').value = '';
    document.getElementById('tag-input').value = '';

    // Create an object to send as JSON data

    let data = {
        "memo": diaryText,
        "tags": tagInput
    };

    // Send POST request to /add_diary endpoint
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/add_diary", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Diary entry successfully added, you can update the UI here if needed
                console.log("Diary entry added successfully");
                showFlashMessage("Diary entry added successfully", "green", "white", 3000);

                // Reload the page after 3 seconds
                setTimeout(function () {
                    location.reload();
                }, 1000);
            } else {
                // Handle errors here
                console.error("Error adding diary entry:", xhr.responseText);
            }
        }
    };

    // Convert data object to JSON string before sending
    xhr.send(JSON.stringify(data));
}

let _memo_id = 0;

function editDiary(memo_id, memo, tag) {
    document.getElementById('diary-text').value = memo;
    document.getElementById('tag-input').value = tag;
    _memo_id = memo_id;
    // Show Apply button and hide Add button
    document.getElementById('add-button').style.display = 'none';
    document.getElementById('apply-button').style.display = 'block';
}

function applyEdit() {
    // Get updated memo and tag values
    let memo = document.getElementById('diary-text').value;
    let tag = document.getElementById('tag-input').value;

    let data = {
        "memo_id": _memo_id,
        "memo": memo,
        "tags": tag
    };

    // Send POST request to /add_diary endpoint
    let xhr = new XMLHttpRequest();
    xhr.open("PUT", "/edit_diary", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {

                console.log("Diary entry edited successfully");
                showFlashMessage("Diary entry edited successfully", "yellow", "black", 1000);
                document.getElementById('add-button').style.display = 'block';
                document.getElementById('apply-button').style.display = 'none';
                // Reload the page after 3 seconds
                setTimeout(function () {
                    location.reload();
                }, 1000);
            } else {
                // Handle errors here
                console.error("Error editing diary entry:", xhr.responseText);
            }
        }
    };

    // Convert data object to JSON string before sending
    xhr.send(JSON.stringify(data));


}


// Function to delete diary entry
function deleteDiaryEntry(memo_id) {
    // Delete diary entry code goes here
    // After successful deletion, display flash message
    let data = {
        "memo_id": memo_id
    }
    let xhr = new XMLHttpRequest();
    showFlashMessage("Diary entry deleted successfully", "red", 1000);
    xhr.open("DELETE", "/delete_diary", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Diary entry successfully added, you can update the UI here if needed
                console.log("Diary entry successfully deleted");
                showFlashMessage("Diary entry successfully deleted", "red", "white", 1000);


                setTimeout(function () {
                    location.reload();
                }, 1000);
            } else {
                // Handle errors here
                console.error("Error adding diary entry:", xhr.responseText);
            }
        }
    };

    // Convert data object to JSON string before sending
    xhr.send(JSON.stringify(data));
}

// Example usage:
// Call deleteDiaryEntry() function after successful deletion
// deleteDiaryEntry();
