<template>
  <div ref="results">
    <section class="search-results__section">
      <div class="search-results__heading">
        <h2 class="heading">Your top matches</h2>
        <p class> Search results for "{{ query }}"</p>
      </div>
      <div class="search-results__container">
        <AsyncStoreCard
            v-for="(store, i) in stores"
            :key="i"
            :store="store"
        />
      </div>
    </section>
  </div>
</template>

<script>
import { defineAsyncComponent } from 'vue';
import SearchLoading from './SearchLoading.vue';
import SearchError from './SearchError.vue';

const AsyncStoreCard = defineAsyncComponent({
  loader: () => import('./StoreCard.vue' /* webpackChunkName: "StoreCard" */),
  loading: SearchLoading,
  delay: 100, // Delay before loading StoreCard component
  error: SearchError,
  timeout: 3000 // If async component hasn't loaded in this time, show Error component
});

export default {
  name: 'SearchResults',
  components: {
    AsyncStoreCard
  },
  props: [
    'stores',
    'query'
  ],
  data() {
    return {
      store: 'store'
    }
  },
  updated() {
    // TODO: fix - currently only second click takes you to results div
    this.scrollToResults();
  },
  methods: {
    scrollToResults() {
      this.$refs.results.scrollIntoView({behavior: 'smooth', block: 'start', inline: 'nearest'});
    }
  }
}
</script>
