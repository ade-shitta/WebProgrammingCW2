<template>
  <div class="mt-3">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3>Character List</h3>
      <button class="btn btn-primary" @click="showAddModal">Add New Character</button>
    </div>

    <CharacterTable 
      :characters="characters"
      @edit="editCharacter"
      @delete="deleteCharacter"
    />

    <!-- Add/Edit Modal -->
    <div class="modal fade" id="characterModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? 'Edit' : 'Add' }} Character</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="mb-3">
                <label class="form-label">Name</label>
                <input type="text" class="form-control" v-model="form.name" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Description</label>
                <textarea class="form-control" v-model="form.description" required></textarea>
              </div>
              <div class="mb-3">
                <label class="form-label">Birth Date</label>
                <input type="date" class="form-control" v-model="form.birth_date">
              </div>
              <div class="mb-3">
                <label class="form-label">Age</label>
                <input type="number" class="form-control" v-model="form.age" required>
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
import CharacterTable from './CharacterTable.vue'

export default {
  components: {
    CharacterTable
  },
  data() {
    return {
      characters: [],
      isEditing: false,
      currentId: null,
      modal: null,
      form: {
        name: '',
        description: '',
        birth_date: '',
        age: 0
      }
    }
  },
  mounted() {
    this.fetchCharacters()
    this.modal = new Modal(document.getElementById('characterModal'))
  },
  setup() {
    const triggerRefresh = inject('triggerRefresh')
    return { triggerRefresh }
  },
  methods: {
    async fetchCharacters() {
      const response = await fetch('http://localhost:8000/api/character/')
      const data = await response.json()
      this.characters = data.characters
    },
    showAddModal() {
      this.isEditing = false
      this.resetForm()
      this.modal.show()
    },
    editCharacter(character) {
      this.isEditing = true
      this.currentId = character.id
      this.form = { ...character }
      this.modal.show()
    },
    resetForm() {
      this.form = {
        name: '',
        description: '',
        birth_date: '',
        age: 0
      }
    },
    async submitForm() {
      const url = this.isEditing 
        ? `http://localhost:8000/api/character/${this.currentId}/`
        : 'http://localhost:8000/api/character/'
      
      const response = await fetch(url, {
        method: this.isEditing ? 'PUT' : 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.form)
      })

      if (response.ok) {
        this.modal.hide()
        this.fetchCharacters()
        this.resetForm()
        this.triggerRefresh()
      }
    },
    async deleteCharacter(id) {
      if (confirm('Are you sure you want to delete this character?')) {
        const response = await fetch(`http://localhost:8000/api/character/${id}/`, {
          method: 'DELETE'
        })
        if (response.ok) {
          this.fetchCharacters()
          this.triggerRefresh()
        }
      }
    }
  }
}
</script>
