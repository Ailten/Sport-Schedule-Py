
window.addEventListener('load', _ => {

    // set default calendar.
    currentDate = new Date();
    monthPicker = document.getElementById('month-picker');
    currentMonth = currentDate.getMonth() +1;  // ajust month from starting to 0.
    currentMonthStr = (currentMonth < 10 ? '0': '') + currentMonth;
    monthPicker.value = `${currentDate.getFullYear()}-${currentMonthStr}`;
    currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth() +1, currentDate.getDate());
    generateCalendar(currentDate);

    // set event change, to actualise calendar.
    monthPicker.addEventListener('change', (evnt) => {
        yearsAndMonthArr = [...evnt.target.value.matchAll(/[0-9]{2,}/g)].map(e => Number(e));
        generateCalendar(new Date(yearsAndMonthArr[0], yearsAndMonthArr[1], 1));
    });
    
});


function generateCalendar(datePick) {

    // get dom container calendar.
    let calendarGrid = document.getElementById('calendarGrid');
    calendarGrid.innerText = '';

    // get year and month from obj date.
    let year = datePick.getFullYear();
    let month = datePick.getMonth() -1;  // ajust month from starting to 0.
    let dateToday = new Date();

    let firstDay = new Date(year, month, 1).getDay();
    let startingDay = firstDay === 0 ? 6 : firstDay - 1;
    let daysInMonth = new Date(year, month + 1, 0).getDate();
    let countDayOfWeek = 0;

    // fill empty days before.
    for (let i = 0; i < startingDay; i++) {
        let currentCell = calendarGrid.appendChild(document.createElement('div'));
        currentCell.classList.add('day-none', 'border', 'rounded', 'm-1');
        countDayOfWeek++;
    }
    // fill days.
    for (let day = 1; day <= daysInMonth; day++) {
        let dayCell = calendarGrid.appendChild(document.createElement('div'));
        dayCell.classList.add('card', 'day-card', 'border', 'rounded', 'm-1', 'p-2', 'd-flex', 'flex-column', 'justify-content-between');
        if (day === dateToday.getDate() && month === dateToday.getMonth() && year === dateToday.getFullYear()) {
            dayCell.classList.add('today');
        } 
        if (countDayOfWeek % 7 >= 5){
            dayCell.classList.add('week-end');
        }
        

        // fill day div.
        dayNum = dayCell.appendChild(document.createElement('div'));
        dayNum.classList.add('text-start', 'day-number');
        dayNum.innerText = day;

        lineUnderDay = dayCell.appendChild(document.createElement('div'));
        lineUnderDay.classList.add('text-end', 'text-muted', 'small', 'line-under-day');
        //lineUnderDay.innerText = '---';

        // icones.
        icoA = lineUnderDay.appendChild(document.createElement('a'));
        icoA.setAttribute('src', '#');  // valide all the day.
        ico = icoA.appendChild(document.createElement('i'));
        ico.classList.add('bi', 'bi-check-lg');

        icoA = lineUnderDay.appendChild(document.createElement('a'));
        icoA.setAttribute('src', '#');  // open page details day.
        ico = icoA.appendChild(document.createElement('i'));
        ico.classList.add('bi', 'bi-three-dots');


        // event for z-index:
        dayCell.addEventListener('mouseover', (evnt) => {
            evnt.target.style.zIndex = '10';
        })
        dayCell.addEventListener('mouseout', (evnt) => {
            evnt.target.style.zIndex = '0';
        })

        countDayOfWeek++;
    }
}