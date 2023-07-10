<template>
    <section>
      <h1>Edit task</h1>
      <hr/><br/>
  
      <form @submit.prevent="submit">
                <div class="mb-3">
                    <label for="title" class="form-label">Title:</label>
                    <input type="text" name="title" v-model="form.title" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="comments" class="form-label">Comments:</label>
                    <input type="textarea" name="comments" v-model="form.comments" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="priority_level" class="form-label">Priority Level:</label>
                    <input type="int" min="1" max="5" name="priority_level" v-model="form.priority_level" class="form-control">
                </div>
                <div class="mb-3">
                    <label for="due_date" class="form-label">Due Date:</label>
                    <input type="date" name="due_date" v-model="form.due_date" class="form-control">
                </div>
                <button class="btn btn-primary" type="submit">Submit</button>
            </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'EditTask',
    props: ['id'],
    data() {
      return {
        form: {
          title: '',
          comments: '',
          priority_level: 0,
          due_date: new Date(),
        },
      };
    },
    created: function() {
      this.GetTask();
    },
    computed: {
      ...mapGetters({ task: 'stateTask' }),
    },
    methods: {
      ...mapActions(['updateTask', 'viewTask']),
      async submit() {
      try {
        let task = {
          id: this.id,
          form: this.form,
        };
        await this.updateTask(task);
        this.$router.push({name: 'Task', params:{id: this.task.id}});
      } catch (error) {
        console.log(error);
      }
      },
      async GetTask() {
        try {
          await this.viewTask(this.id);
          this.form.title = this.task.title;
          this.form.comments = this.task.comments;
          this.form.priority_level = this.task.priority_level;
          this.form.due_date = this.task.due_date;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      }
    },
  });
  </script>