/*todo : 
1. Рефакторинг с классами
2. Форма должна поддерживать чекбоксы радиокнопки, текстареа, селекты
3. Форма должна быть вложена и могла бы работать с json схема 
4. Стили прикрутить 
5. Валидация формы
 */

/* 
Required - обязательность заполнения, по умолчанию false
placeholder 
hints
disabled,tabindex ???????
Checkbox
   {     
         "label": "Запомнить",
         "type": "checkbox"
         "items":[
               {
               "cheked": "true",
               "value": "yes"},
                 {
               "cheked": "false",
               "value": "no"}
         ] 
      },
Password
      {
         "label": "Пароль",
         "type": "password",
      },
Textarea
      {  
         type: "textarea"
         "label": "story",
         "placeholder": "подпись поля"
      } 
Radio
      {
         "type":"radio",
         "name": "beer",
         "item" : [
            { value:"lager"},
            { value: "dark" }
         ]
      }  
      
File {
      "type": "file",
      "name": "photo"
},

Selector {
    selected?
   name : "color"
   id: "color"
   option : [{
      value: "red"
      text : "Красный"
   },
   {
      value: "yellow"
      text : "Желтый"
   },
   ]
}

MultipluySelector {
   selected?
   name : "color"
   id: "color"
   multiple : true
   option : [{
      value: "red"
      text : "Красный"
   },
   {
      value: "yellow"
      text : "Желтый"
   },
   ]
}
      
      */

const input = `{
   "inputs": [
     {
     "label": "Фамилия",
     "type": "text",
     "id": "last_name",
     "placeholder": "Vasiya"
     "hints": ["нарусском","безпробелов"]
     },
     {
     "label": "Возраст",
     "type": "number",
     "id": "age"
     },
     {
      "label": "A multiple choices list",
      "type": "checkbox",
      "items": [
            {
            "cheked": "true",
            "value": "yes",
            "id": "ch1"
            },
            {
            "cheked": "false",
            "value": "no",
            "id": "ch2"
         }
      ] 
   }
 ],
   "submit": {
     "url": "www.example.com",
     "text": "Отправить"
   },
   "style" : "dark"
 }`

class JsonForm {
   constructor (element, options) {
      this.element = element;
      this.shema = JSON.parse(options.shema)
      this.style = this.shema.style ? this.shema.style : "light"
   }
   initForm() {
      this.form = document.createElement('form')
      this.element.append(this.form)
   }
   renderInputs() {
      this.shema.inputs.forEach(element => {
         const field = document.createElement('input')
         const label = document.createElement('label')
         field.id = element.id;
         field.type = element.type;
         label.innerHTML = element.label
         this.form.append(label)
         label.append(field)
      })
   }
   // renderCheckBox() {
   //    this.shema.checkbox.items.forEach(element => {
   //       const checkbox = document.createElement("input")
   //       checkbox.type = this.shema.checkbox.type
   //       checkbox.checked = element.checked
   //       checkbox.value = element.value
   //    })


   // }
   renderSubmit() {
      const submit = document.createElement("input")
      submit.type = "submit"
      submit.value = this.shema.submit.text
      this.form.append(submit)
   }
   render() {
      this.initForm()
      this.renderInputs()
      this.renderSubmit()
      // this.renderCheckBox()
   }
}



const formContainer = document.getElementById("start_form")

const Test = new JsonForm(formContainer, { shema: input })
Test.render()



