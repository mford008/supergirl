title: Blog
author: Maddy Ford
data = '''
  <div class="container">
      <div class="row">
        <div class="col">
          <h1>Thought Collector: A Tech Blog</h1>
          <p>This is a compilation of all the amazing tips and advice I've
            received throughout my professional transition into a tech career.</p>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <h2><a href="{{blog_post_output_filepath}}">{{test_one}}</a></h2>
          <h3>{{date_one}}</h3>
          <h2><a href="{{blog_post_output_filepath}}">{{test_two}}</a></h2>
          <h3>{{date_two}}</h3>
          <h2><a href="{{blog_post_output_filepath}}">{{test_three}}</a></h2>
          <h3>{{date_three}}</h3>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <p>{{blog_text}}</p>
        </div>
      </div>
    </div>
'''