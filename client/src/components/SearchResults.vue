<template>
  <div>
    <section class="search-results__section">
      <div class="search-results__heading">
        <h2 class="heading">Your top matches</h2>
        <p class> Search results for "{{ query }}"</p>
      </div>
      <div class="search-results__container">
        <StoreCard
            v-for="(store, i) in stores"
            :key="i"
            :store="store"/>
      </div>
    </section>
  </div>
</template>

<script>
import StoreCard from './StoreCard.vue';

export default {
  name: 'SearchResults',
  components: {
    StoreCard
  },
  props: [
    'stores',
    'query'
  ],
  data() {
    return {
      store: 'store'
    }
  }
}
</script>
