

vi_id = {
    1: 'falimi.mp4',
    2:'sbnp.mp4',
    # Add more video IDs and paths as needed
}

@app.route('/player/<int:video_id>')
def player(video_id):
   
    video_file = vi_id.get(video_id)
    
    if video_file is not None:
        # Construct the correct video path relative to the 'static' folder
        video_path = f'/static/videos/{video_file}'  # Notice the leading slash here
        return render_template('player.html', video_path=video_path)
    else:
        return "Video not found", 404

@app.route('/watch/<int:button_id>')
def watch_video(button_id):
    if button_id in vi_id:
        return redirect(url_for('player', video_id=button_id))
    else:
        return "Video not found", 404


#note this is not the full code of flask app  this is the code for media  player 





