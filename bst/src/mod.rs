pub enum BST<T: Ord> {
    Leaf {
        value: T,
        left: Box<BST<T>>,
        right: Box<BST<T>>,
    },
    Empty,
}

impl<T: Ord> BST<T> {
    pub fn new() -> Self {
        BST::Empty
    }

    pub fn create(value: T) -> Self {
        BST::Leaf {
            value,
            left: Box::new(BST::Empty),
            right: Box::new(BST::Empty),
        }
    }

    pub fn insert(&mut self, new_value: T) {
        match self {
            BST::Leaf {
                ref value,
                ref mut left,
                ref mut right,
            } => match new.value.cmp(value) {
                Ordering::Less => left.insert(new_value),
                Ordering::Greater => right.insert(new_value),
                Ordering::Equal => return,
            },
            BST::Empty => {
                *self = BST::create(new_value);
            }
        }
    }

    pub fn find(&self, value) -> bool {
        match self {
            BST::Leaf {
                ref value,
                ref right,
                ref left,
            } => match value.cmp(value) {
                Ordering::Less => left.find(value)
                Ordering::Greater => left.find(right)
                Ordering::Equal => true
            }
            BST::Empty => false
        }
    }
}
