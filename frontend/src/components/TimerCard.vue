<template>
  <section class="c-timer-card o-section">
    <div class="c-timer-card__container o-container">
      <div class="circular-timer">
        <svg
          class="progress-ring"
          width="120"
          height="120"
          viewBox="0 0 120 120"
        >
          <!-- Background circle -->
          <circle
            class="progress-ring-circle background-circle"
            :stroke="backgroundStrokeColor"
            :stroke-dasharray="circumference"
            stroke-width="8"
            fill="transparent"
            r="50"
            cx="60"
            cy="60"
          />
          
          <!-- Progress circle -->
          <circle
            class="progress-ring-circle"
            :stroke-dasharray="circumference"
            :stroke-dashoffset="circumference * progress"
            :stroke="progressStrokeColor"
            stroke-width="8"
            fill="transparent"
            r="50"
            cx="60"
            cy="60"
            transform="rotate(-90 60 60)"
          />


          <!-- Text time element -->
          <text
            x="50%"
            y="50%"
            text-anchor="middle"
            alignment-baseline="middle"
            :class="timerTextClass"
            :style="{ fill: textColor }"
          >
            {{ formatTime(hours, minutes, seconds) }}
          </text>
        </svg>
        <!-- Time Note -->
        <text
          v-if="timerString"
          x="50%"
          y="70%"
          text-anchor="middle"
          alignment-baseline="middle"
          class="timer-string"
        >
          {{ timerString }}
        </text>
      </div>
    </div>
  </section>
</template>


<script setup>
import { ref, watch, computed, onMounted, onUnmounted } from 'vue'

//incoming time length and note
const props = defineProps({
    initialTime: {
        type: Number,
        required: true
    },
    timerString: {
        type: String,
        default: ''
    },
    stepGeneratedOn:{
        type: Number,
        required: true
    }
  
})

let remainingTime = ref(props.initialTime)
const totalTime = props.initialTime
const stepGeneratedOn = props.stepGeneratedOn

const hours = ref(0)
const minutes = ref(0)
const seconds = ref(0)
let countdownInterval

const emit = defineEmits(['countdownEnd']) // Define emitted events

const radius = 50
const circumference = 2 * Math.PI * radius
const progress = ref(0)

const flashText = ref(false)

onMounted(startCountdown)
onUnmounted(() => {
    if (countdownInterval) {
        clearInterval(countdownInterval)
    }
})


/*
 * Setup dynamic colours here
 */

const textColor = computed(() => {
    return remainingTime.value <= 0 ? '#e74c3c' : '#333' // Red color when completed, otherwise black
})

const progressStrokeColor = computed(() => {
  if (flashText.value) {
        return 'transparent'; // Transparent color when flashing
    } else {
        return '#3498db'; // Blue color for background circle
    }
})

const backgroundStrokeColor = computed(() => {
    if(remainingTime.value <= 0){
        return '#333'
    }
    return `rgb(204, 204, 204, ${1 - progress.value})` // Grey color for progress circle
})

/*
 * Class switchers
 */
const timerTextClass = computed(() => {
    return {
        'timer-text': true,
        'timer-text-flash': flashText.value,
    }
})

/*
 * String formatting
 */
function formatTime(h, m, s) {
  if (flashText.value) {
        return '00:00:00';
    } else {
        return `${pad(h)}:${pad(m)}:${pad(s)}`;
    }
}

function pad(value) {
    return value.toString().padStart(2, '0')
}

/*
 * Timer logic
 */

function startCountdown() {
    countdownInterval = setInterval(() => {
        remainingTime.value -= 1000
        if (remainingTime.value <= 0) {
            clearInterval(countdownInterval)
            emit('countdownEnd',props.stepGeneratedOn)
        }
    }, 1000)
}

function updateTime() {
    hours.value = Math.floor(remainingTime.value / (60 * 60 * 1000))
    let remaining = remainingTime.value % (60 * 60 * 1000)
    minutes.value = Math.floor(remaining / (60 * 1000))
    remaining %= (60 * 1000)
    seconds.value = Math.floor(remaining / 1000)
    updateProgress()
}

function updateProgress() {
    progress.value = 1 - remainingTime.value / totalTime
}

watch(remainingTime, (newVal, oldVal) => {
    updateTime()
    if (newVal <= 0) {
        flashText.value = true
    }
})


</script>

<style scoped>
.timer-text {
  font-size: 1.5em;
  fill: #333;
  font-weight: bold;
}
.timer-text-flash {
  animation: flash 1s infinite alternate;
}

.timer-string {
  font-size: 1em;
  fill: #777;
}

.circular-timer {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.progress-ring {
  display: block;
}

.background-circle {
  stroke-width: 8;
}
.progress-ring-circle {
  stroke-linecap: round;
  transition: stroke 0.5s; /* Add transition for smooth color change */
}
.completed-circle {
  stroke-linecap: round;
  transition: stroke 0.5s; /* Add transition for smooth color change */
}

@keyframes flash {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}


</style>
