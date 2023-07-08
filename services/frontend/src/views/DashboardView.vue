<template>
    <div>
        <section>
            <h1>Add new task</h1>
            <hr><br>
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

        <br><br>
        
        <section>
            <h1>Tasks</h1>
            <hr><br>

            <div v-if="tasks.length">
                <div v-for="task in tasks" :key="task.id" class="notes">
                    <div class="card" style="widht: 18rem;">
                        <div class="card-body">
                            <ul>
                                <li><strong>Task Title:</strong> {{ task.title }}</li>
                                <li><strong>Comments:</strong> {{ task.comments }}</li>
                                <li><strong>Priority Level:</strong> {{ task.priority_level }}</li>
                                <li><strong>Due Date:</strong> {{ task.due_date }}</li>
                                <li><router-link :to="{name: 'Task', params:{id: task.id}}">View</router-link></li>
                            </ul>
                        </div>

                    </div>

                </div>

            </div>
            <div v-else>
                <p>Nothing to see. Go add some tasks</p>
            </div>
        </section>
    </div>
</template>



<script>
import { defineComponent } from 'vue';
import { mapGetters,mapActions } from 'vuex';

export default defineComponent({
    name:'Dashboard',
    data(){
        return{
            form:{
                title:'',
                comments:'',
                priority_level:0,
                due_date: new Date(),
            },
        };
    },
    created: function(){
        return this.$store.dispatch('getTasks');
    },
    computed:{
        ...mapGetters({tasks: 'stateTasks'}),
    },
    methods:{
        ...mapActions(['createTask']),
        async submit(){
            await this.createTask(this.form);
        },
    },
});

</script>

<!--We'll configure the route and view here shortly, but the key thing to take away is that the route takes in the note ID and sends the user to the corresponding route -- e.g., note/1, note/2, note/10, note/101, and so forth.

The created function is called during the creation of the component, which hooks into the component lifecycle. In it, we called the mapped getNotes action.-->