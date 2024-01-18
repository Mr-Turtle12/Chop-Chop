<template>
  <section class="c-timer-card o-section">
    <div class="c-timer-card__container o-container">
      <div class="circular-timer">
        <svg class="progress-ring" width="120" height="120" viewBox="0 0 120 120">
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
          ></circle>
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
          ></circle>
          <text x="50%" y="50%" text-anchor="middle" alignment-baseline="middle" class="timer-text">
            {{ formatTime(hours, minutes, seconds) }}
          </text>
        </svg>
        <text x="50%" y="70%" text-anchor="middle" alignment-baseline="middle" class="timer-string" v-if="timerString">
            {{ timerString }}
          </text>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, watch, computed, onMounted, onUnmounted, defineProps, defineEmits } from 'vue';

const props = defineProps({
  initialTime: {
    type: Number,
    required: true
  },
  timerString: {
    type: String,
    default: ''
  }
});

const emit = defineEmits(['countdownEnd']); // Define emitted events


let remainingTime = ref(props.initialTime);
const totalTime = props.initialTime;

const hours = ref(0);
const minutes = ref(0);
const seconds = ref(0);

const radius = 50;
const circumference = 2 * Math.PI * radius;
const progress = ref(0);

function formatTime(h, m, s) {
  return `${pad(h)}:${pad(m)}:${pad(s)}`;
}

function pad(value) {
  return value.toString().padStart(2, '0');
}

function updateTime() {
  hours.value = Math.floor(remainingTime.value / (60 * 60 * 1000));
  let remaining = remainingTime.value % (60 * 60 * 1000);
  minutes.value = Math.floor(remaining / (60 * 1000));
  remaining %= (60 * 1000);
  seconds.value = Math.floor(remaining / 1000);
  updateProgress();
}

function updateProgress() {
  progress.value = 1 - remainingTime.value / totalTime;
}

watch(remainingTime, updateTime);

let countdownInterval;

function startCountdown() {
  countdownInterval = setInterval(() => {
    remainingTime.value -= 1000;
    if (remainingTime.value <= 0) {
      clearInterval(countdownInterval);
      emit('countdownEnd',props.timerString);
    }
  }, 1000);
}

onMounted(startCountdown);
onUnmounted(() => {
  if (countdownInterval) {
    clearInterval(countdownInterval);
  }
});

const progressStrokeColor = computed(() => {
  return '#3498db'; // Blue color for background circle
});

const backgroundStrokeColor = computed(() => {
  return `rgb(204, 204, 204, ${1 - progress.value})`; // Grey color for progress circle
});
</script>

<style scoped>
.timer-text {
  font-size: 1.5em;
  fill: #333;
  font-weight: bold;
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
}
</style>
