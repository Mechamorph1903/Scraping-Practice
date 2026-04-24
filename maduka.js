const mOverlay = document.getElementById("maduka-overlay");
const mScreen1_Choice = document.getElementById("maduka-screen1");
const mScreen2_Link = document.getElementById("maduka-screen2");
const mScreen3Bad_Result = document.getElementById("maduka-screen3");
const mAutofill_Choice = document.getElementById("maduka-auto-btn");
const mManual_Choice = document.getElementById("maduka-manual-entry-btn");
const mURL_Input = document.getElementById("maduka-url-input");
const mFetch = document.getElementById("maduka-fetch-btn");
const mErrorDisplay = document.getElementById("maduka-error-reason");
const mRetry_Result = document.getElementById("maduka-retry-btn");
const mManual_Result = document.getElementById("maduka-fallback-btn");
const mloading_screen = document.getElementById("loading_screen");
const mScreen2_main = document.getElementById("screen2_main");
const warn = document.getElementById("warn");
const case1 = document.getElementById("dot1");
const case2 = document.getElementById("dot2");
const case_div = document.querySelector(".elements_div");
const heart = document.querySelector("#heart")
const fetch_text = document.getElementById("fetch-text");
let job_details = null;
let successhandled = false;
let failHandled = false;

function showMaduka() {
    mOverlay.style.display = 'flex';
    mOverlay.style.opacity = '1';
}

function closeMaduka() {
    mOverlay.classList.add('closing')

    mOverlay.addEventListener("transitionend", (e) => {
        mOverlay.style.display = 'none';
        mOverlay.classList.remove('closing')
    }, {once: true})


}

function showMadukaScreen(screen_no) {
    mScreen1_Choice.style.display = 'none';
    mScreen2_Link.style.display = 'none';
    mScreen3Bad_Result.style.display = 'none';
    mloading_screen.style.display = 'none';
    mScreen2_main.style.display = 'none'

    switch(screen_no) {
        case 2:
            mScreen2_Link.style.display = 'flex';
            mScreen2_main.style.display = 'flex';
            break;
        case 3:
            mScreen3Bad_Result.style.display = 'flex';
            break;
        case 4:
            mScreen2_Link.style.display = 'flex';
            mloading_screen.style.display = 'flex';
            break;
        default:
            mScreen1_Choice.style.display = 'flex';
    }
}

function triggerSuccess(){
    console.log('case_div:', case_div)
    console.log('case1:', case1)
    case_div.classList.add("success-anim");
    fetch_text.innerText = `Details Found!`

    case1.addEventListener("transitionend", (e) => {
        if (e.propertyName === 'opacity' && !successhandled){
            successhandled = true;
            console.log('dots faded, ready for next phase');
            case_div.classList.add('flying')
        }
    }, { once: true })

    case2.addEventListener('animationend', (e) =>{
        if (e.animationName === "flyUp"){
            closeMaduka()
            console.log('sky high, now for the finale');

        }
    },{ once: true })
    return;
}


function triggerFail() {
    case_div.classList.add("failed");
    fetch_text.innerText = "Fetch Unsuccessful";

    case1.addEventListener("transitionend", (e) => {
        if (e.propertyName === "opacity" && !failHandled) {
            failHandled = true;
            case_div.classList.add("show-heart");
        }
    }, { once: true });

    heart.addEventListener("transitionend", (e) => {
        if (e.propertyName === "opacity"){
            setTimeout(() => fadeToScreen3(), 2000)
        }
    }, { once: true })

    
}

mAutofill_Choice.addEventListener("click",(e) => {
    showMadukaScreen(2);
    return;
})

mManual_Choice.addEventListener("click", (e) => {
    closeMaduka();
})


// replace your fetch call with this temporarily
async function mockFetch(url) {
    // simulate network delay
    await new Promise(resolve => setTimeout(resolve, 5000))
    
    // return fake success response
    return {
        status: true,
        reason: null,
        job_name: "Software Engineer, Full Stack",
        company_name: "Figma",
        location: "San Francisco, CA · Remote",
        role_name: "Full Stack Engineer",
        work_arrangement: "Hybrid",
        deadline: null,
        job_description: "This is a test job description."
    }
}

// and a mock fail response to test the fail screen
async function mockFetchFail(url) {
    await new Promise(resolve => setTimeout(resolve, 2000))
    return {
        status: false,
        reason: "This page requires a login to access."
    }
}


mFetch.addEventListener("click", async (e) => {
    const value = mURL_Input.value;
    warn.innerText = ``;
    if (!value){
        warn.innerText = `Please provide a valid link`;
        return;
    }

    showMadukaScreen(4);

    // const response = await fetch('/applications/parse-job', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify({ url: mURL_Input.value.trim() })
    // })

    // const data = await response.json();

    const data = await mockFetch(mURL_Input.value);
    

    if (!data || !data.status){
        triggerFail();
        return;
    }
    triggerSuccess();

    // closeMaduka();
    console.log(response);
    return;
})


mRetry_Result.addEventListener("click", (e) => {
    case_div.classList.remove("show-heart");
    case_div.classList.remove("failed");
    fetch_text.innerHTML = `Fetching details<span>.</span><span>.</span><span>.</span>`;
    case_div.classList.remove("success-anim");
    case_div.classList.remove("success-anim");
    failHandled = false;
    successhandled = false;
    mScreen2_Link.style.opacity = '1';

    showMadukaScreen(2);
    return;
})

mManual_Result.addEventListener("click", (e) => {
    closeMaduka();
    return;
})


function fadeToScreen3(){
    mScreen2_Link.style.opacity = '0';

    mScreen2_Link.addEventListener('transitionend', (e) => {
        if (e.propertyName === "opacity"){
            mScreen2_Link.style.display = 'none'
            mScreen3Bad_Result.style.display = 'flex'
            mScreen3Bad_Result.style.opacity = '0';

            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    mScreen3Bad_Result.style.opacity = '1'
                })
            })
        }
    }, { once: true })
}