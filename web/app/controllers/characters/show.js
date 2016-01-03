import Ember from 'ember';

export default Ember.Controller.extend({
  sortedLevelsBy: ['level:desc', 'exp_at:desc', 'name'],
  sortedLevels: Ember.computed.sort('model.levels', 'sortedLevelsBy'),
});
