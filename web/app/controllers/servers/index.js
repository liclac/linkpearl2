import Ember from 'ember';

export default Ember.Controller.extend({
  sortedServersBy: ['population:desc', 'name'],
  sortedServers: Ember.computed.sort('model', 'sortedServersBy'),
  populationData: Ember.computed('model', function() {
    let model = this.get('model');
    let data = [];
    this.get('model').forEach(function(server) {
      data.push({
        value: server.get('population'),
        label: server.get('name'),
      });
    });
    return data;
  }),
});
