
//cashfund

document.querySelectorAll('body > ion-app > ion-modal > div > numpad > ion-content > div.scroll-content > ion-item > div.item-inner > div > ion-input > input').value = "09";
//save
document.querySelectorAll('body > ion-app > ion-modal > div > numpad > ion-content > div.scroll-content > div > ion-grid > ion-row:nth-child(5) > ion-col:nth-child(3) > button')[0].click();


others = document.querySelectorAll('.item-cover.item-cover-md.item-cover-default.item-cover-default-md')
per= 0
others[per].click()

document.querySelectorAll(".items.button-md.item.item-block.item-md.item-checkbox")[0].innerText.replace('\nD','');

var index = 0;
var find_element = false;
while (find_element == false){
    if(document.querySelectorAll(".items.button-md.item.item-block.item-md.item-checkbox")[index].innerText.replace('\nD','') =="MOJOS OVERLOAD");
    {
        find_element = true; 
    }
    document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[index].innerText;
    index++;
}if(find_element)
{
    document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[index-1].click();
}

var index = 0;var find_element = false;while (find_element == false){if(document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[index].innerText.replace('\nD','') =="MOJOS OVERLOAD"){find_element = true; }document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[index].innerText;index++;}if(find_element){document.querySelectorAll('.items.button-md.item.item-block.item-md.item-checkbox')[index-1].click();}