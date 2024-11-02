<template>
  <div class="mt-3">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3>Anime List</h3>
      <button class="btn btn-primary" @click="showAddModal">Add New Anime</button>
    </div>

    <AnimeTable 
      :animes="animes" 
      @edit="editAnime" 
      @delete="deleteAnime"
    />

    <!-- Add/Edit Modal -->
    <div class="modal fade" id="animeModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? 'Edit' : 'Add' }} Anime</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="mb-3">
                <label class="form-label">Title</label>
                <input type="text" class="form-control" v-model="form.title" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Description</label>
                <textarea class="form-control" v-model="form.description" required></textarea>
              </div>
              <div class="mb-3">
                <label class="form-label">Release Date</label>
                <input type="date" class="form-control" v-model="form.release_date" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Episodes</label>
                <input type="number" class="form-control" v-model="form.episodes" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Rating (1-10)</label>
                <input type="number" class="form-control" v-model="form.rating" min="1" max="10" required>
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" v-model="form.is_ongoing">
                <label class="form-check-label">Is Ongoing</label>
              </div>
              <div class="text-end">
                <button type="button" class="btn btn-secondary me-2" data-bs-dismiss="modal">Cancel</button>
                <button type="submit" class="btn btn-primary">Save</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from 'bootstrap'
import { inject } from 'vue'
import AnimeTable from './AnimeTable.vue'

export default {
  components: {
    AnimeTable
  },
  data() {
    return {
      animes: [],
      isEditing: false,
      currentId: null,
      modal: null,
      form: {
        title: '',
        description: '',
        release_date: '',
        episodes: 0,
        rating: 1,
        is_ongoing: true
      }
    }
  },
  mounted() {
    this.fetchAnimes()
    this.modal = new Modal(document.getElementById('animeModal'))
  },
  setup() {
    const triggerRefresh = inject('triggerRefresh')
    return { triggerRefresh }
  },
  methods: {
    async fetchAnimes() {
      const response = await fetch('http://localhost:8000/api/anime/')
      const data = await response.json()
      this.animes = data.animes
    },
    showAddModal() {
      this.isEditing = false
      this.resetForm()
      this.modal.show()
    },
    editAnime(anime) {
      this.isEditing = true
      this.currentId = anime.id
      this.form = { ...anime }
      this.modal.show()
    },
    resetForm() {
      this.form = {
        title: '',
        description: '',
        release_date: '',
        episodes: 0,
        rating: 1,
        is_ongoing: true
      }
    },
    async submitForm() {
      const url = this.isEditing 
        ? `http://localhost:8000/api/anime/${this.currentId}/`
        : 'http://localhost:8000/api/anime/'
      
      const response = await fetch(url, {
        method: this.isEditing ? 'PUT' : 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.form)
      })

      if (response.ok) {
        this.modal.hide()
        this.fetchAnimes()
        this.resetForm()
        this.triggerRefresh()
      }
    },
    async deleteAnime(id) {
      if (confirm('Are you sure you want to delete this anime?')) {
        const response = await fetch(`http://localhost:8000/api/anime/${id}/`, {
          method: 'DELETE'
        })
        if (response.ok) {
          this.fetchAnimes()
          this.triggerRefresh()
        }
      }
    }
  }
}
</script>
