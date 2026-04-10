document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".gallery-button");

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const currentRow = button.closest("tr");
            const images = JSON.parse(button.dataset.images || "[]");

            // Check if next row is already a gallery row → toggle (remove)
            const nextRow = currentRow.nextElementSibling;
            if (nextRow && nextRow.classList.contains("gallery-row")) {
                nextRow.remove();
                return;
            }

            // Create new gallery row
            const galleryRow = document.createElement("tr");
            galleryRow.classList.add("gallery-row");

            const cell = document.createElement("td");
            cell.colSpan = 9; // match number of table columns

            const container = document.createElement("div");
            container.classList.add("gallery-container");

            // Take up to 3 images
            const imagesToShow = images.slice(0, 3);

            if (imagesToShow.length === 0) {
                container.textContent = "No images available.";
            } else {
                imagesToShow.forEach((src) => {
                    const img = document.createElement("img");
                    img.src = src;
                    img.alt = "Product image";
                    img.classList.add("gallery-image");
                    container.appendChild(img);
                });
            }

            cell.appendChild(container);
            galleryRow.appendChild(cell);

            // Insert after current row
            currentRow.insertAdjacentElement("afterend", galleryRow);
        });
    });
});