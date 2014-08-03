var spawn = require('child_process').spawn;
var express = require('express');

var app = express();

app.use(express.static(__dirname + '/static'));

app.get('/convert', function(req, res, next) {
  var url = req.query.url;

  if (!/^https?:\/\//.test(url))
    return res.send(400);

  var chunks = [];
  var metadata = spawn('youtube-dl', [
    '--dump-json',
    url
  ]);
  metadata.stdout.on('data', function(chunk) {
    chunks.push(chunk);
  });
  metadata.on('close', function(code) {
    if (code != 0)
      return res.send(404);
    var mp3stream = spawn('youtube-dl', [
      '--extract-audio',
      '--audio-format', 'mp3',
      '--prefer-avconv',
      '--quiet',
      '--no-playlist',
      '--output', '-',
      req.query['url']
   ]);
   res.set('Content-Type', 'audio/mp3');
   res.set('Content-Disposition', 'attachment; filename=audio.mp3');
   mp3stream.stdout.pipe(res);
  });
});

app.listen(3000, function() {
  console.log('ok');
});
