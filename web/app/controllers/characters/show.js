import Ember from 'ember';

export default Ember.Controller.extend({
  sortedLevelsBy: ['level:desc', 'exp_at:desc', 'name'],
  sortedLevels: Ember.computed.sort('model.levels', 'sortedLevelsBy'),
  sortedMinionsBy: ['name'],
  sortedMinions: Ember.computed.sort('model.minions', 'sortedMinionsBy'),
  sortedMountsBy: ['name'],
  sortedMounts: Ember.computed.sort('model.mounts', 'sortedMountsBy'),
});
