const blankForm = document.querySelector("#blank-form");
const attachmentBtn = document.querySelector("#attachment-btn");
const attachmentContainer = document.querySelector("#attachments");
const manageMentFormInputEl = document.querySelector("#id_form-TOTAL_FORMS");

attachmentBtn.addEventListener("click", (event) => {
  event.preventDefault();
  const newBlankForm = blankForm.cloneNode(true);

  newBlankForm.classList.add("attachment-form");
  newBlankForm.classList.remove("hidden");
  newBlankForm.removeAttribute("id");

  //
  const totalFormValue = Number(manageMentFormInputEl.value);
  // console.log("this is total form value::", totalFormValue);
  manageMentFormInputEl.value = totalFormValue + 1;

  const formRegex = new RegExp(`__prefix__`, "g");
  newBlankForm.innerHTML = newBlankForm.innerHTML.replace(
    formRegex,
    totalFormValue
  );

  attachmentContainer.appendChild(newBlankForm);
});

// #id_form-TOTAL_FORMS
