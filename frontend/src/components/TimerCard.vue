<template>
    <section class="c-timer-card o-section">
      <div class="c-timer-card__container o-container">
        <vue-countdown :time="2 * 24 * 60 * 60 * 1000" v-slot="{ days, hours, minutes, seconds }">
            Time Remaining：{{ days }} days, {{ hours }} hours, {{ minutes }} minutes, {{ seconds }} seconds.
        </vue-countdown>
      </div>
    </section>
</template>

<script setup>
import VueCountdown from '@chenfengyuan/vue-countdown'
    


</script>