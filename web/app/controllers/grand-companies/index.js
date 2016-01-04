import Ember from 'ember';

export default Ember.Controller.extend({
  sortedGCsBy: ['members:desc', 'name'],
  sortedGCs: Ember.computed.sort('model', 'sortedGCsBy'),
  membershipData: Ember.computed('model', function() {
    return this.get('model').map(function(gc) {
      return { label: gc.get('name'), value: gc.get('members') };
    });
  }),
});
