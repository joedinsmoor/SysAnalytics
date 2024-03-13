import psutil
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)



@app.route('/system-analytics')
def system_analytics_pretty():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    return render_template(template_name_or_list='sys_analytics.html', 
                           cpu_usage=cpu_usage,
                           memory_usage=memory_usage,
                           disk_usage=disk_usage)

@app.route('/system-analytics-raw')
def system_analytics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    analytics = {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage
    }
    
    return jsonify(analytics)


if __name__ == '__main__':
    app.run(debug=True)


